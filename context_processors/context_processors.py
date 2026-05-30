from blog.models import Article, Category


def recent_articles(request):
    rec_articles = Article.objects.order_by("-created")[:3]
    return {"recent_articles": rec_articles}


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
