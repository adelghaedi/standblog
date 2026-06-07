from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name=_("Title"))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    body = models.TextField(verbose_name=_("Text"))
    image = models.ImageField(upload_to="images/articles", null=True, blank=True, verbose_name=_("Image"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="articles", verbose_name=_("Author"))
    categories = models.ManyToManyField(Category, related_name="articles", verbose_name=_("Categories"))
    is_published = models.BooleanField(verbose_name=_("published"))
    pub_date = models.DateTimeField(default=timezone.now(), verbose_name=_("Publication date"))
    slug = models.SlugField(blank=True, unique=True, verbose_name=_("Article key"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save()

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    def show_image(self):
        if self.image:
            return format_html(
                "<img src='{0}' width='60px' height='50px'>",
                self.image.url,
            )
        return format_html("<h4 style='color: red;'>{0}</h4>", _("There is no image"))

    show_image.short_description = _("Image")

    class Meta:
        ordering = ("-created",)
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        models.CASCADE,
        related_name="comments",
        verbose_name=_("Article"),
    )

    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="comments",
        verbose_name=_("User")
    )

    body = models.TextField(verbose_name=_("Text"))
    created = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey(
        "self",
        models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name=_("Parent Comment")
    )

    def __str__(self):
        return self.body[:30]

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    email = models.EmailField(verbose_name=_("Email"))
    body = models.TextField(verbose_name=_("Text"))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("User")
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("Article")
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.article.title}"

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        ordering = ("-created",)
