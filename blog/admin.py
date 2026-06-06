from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Article, Category, Comment, Message, Like


class ArticleFilterByTitle(admin.SimpleListFilter):
    title = _("Repeated keys")
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ("Morbi", "Morbi"),
            ("Donec", "Donec"),
            ("Etiam", "Etiam")
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())
        return None


class CommentTabularInline(admin.TabularInline):
    model = Comment


class CommentStackedInline(admin.StackedInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("show_image", "__str__", "author", "is_published")
    list_editable = ("author",)
    list_filter = ("is_published", ArticleFilterByTitle)
    search_fields = ("title", "body")
    inlines = (CommentStackedInline,)


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
