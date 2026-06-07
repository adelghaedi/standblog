from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Article, Category, Comment, Message, Like
from .mixins import CustomLoginRequiredMixin


def all_articles_on_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()

    # get page
    page_number = request.GET.get("page", 1)

    # paginator
    paginator = Paginator(articles, 2)
    articles_page = paginator.get_page(page_number)

    return render(request, "blog/article_list.html", {
        "article_list": articles_page
    })


def search_articles(request):
    # search articles
    search_value = request.GET.get("q")
    result_search = Article.objects.filter(title__icontains=search_value)

    # paginator
    page_number = request.GET.get("page")
    paginator = Paginator(result_search, 2)
    result_page = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {"article_list": result_page})


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        article = context.get("article")
        user = self.request.user

        if Like.objects.filter(user_id=user.id, article_id=article.id).exists():
            user_liked_article = True
        else:
            user_liked_article = False

        context["user_liked_article"] = user_liked_article
        return context

    def post(self, request, *args, **kwargs):
        parent_id = request.POST.get("parent_id")

        slug = kwargs.get("slug")

        article = get_object_or_404(Article, slug=slug)

        Comment.objects.create(
            article=article,
            user=request.user,
            body=request.POST.get("body"),
            parent_id=parent_id
        )

        return super().get(request, *args, **kwargs)


class ArticleListView(CustomLoginRequiredMixin, ListView):
    model = Article
    paginate_by = 2


class MessageView(CreateView):
    model = Message
    fields = ("title", "body")
    success_url = reverse_lazy("home:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all()
        return context

    def form_valid(self, form):
        message = form.save(commit=False)
        if self.request.user.is_authenticated:
            message.email = self.request.user.email
        message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("blog:all_messages")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("blog:all_messages")


def like_view(request, slug):
    article = Article.objects.get(slug=slug)
    user = request.user

    if Like.objects.filter(user_id=user.id, article_id=article.id).exists():
        like = Like.objects.get(user_id=request.user.id, article_id=article.id)
        like.delete()
        return JsonResponse({"liked": True})
    else:
        Like.objects.create(user_id=request.user.id, article_id=article.id)
        return JsonResponse({"liked": False})
