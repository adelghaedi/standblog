from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("detail/<str:slug>", views.ArticleDetailView.as_view(), name="article_detail"),
    path("all", views.ArticleListView.as_view(), name="all_articles"),
    path(
        "all_on_category/<int:pk>",
        views.all_articles_on_category,
        name="all_articles_on_category"
    ),
    path("search", views.search_articles, name="search_articles"),
    path("contact_us", views.MessageView.as_view(), name="contact_us"),
    path("message/all", views.MessageListView.as_view(), name="all_messages"),
    path("message/edit/<int:pk>", views.MessageUpdateView.as_view(), name="edit_message"),
    path("message/delete/<int:pk>", views.MessageDeleteView.as_view(), name="delete_message"),
    path("like/<str:slug>", views.like_view, name="like_article")
]
