from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
    path("",ArticleListView.as_view(), name="article-list"),
    # path("create/", article_create_view),
    path("<int:pk>/",ArticleDetailView.as_view(), name="article-detail"),
    # path("<int:id>/update/",article_update_view,name="article-update"),
    # path("<int:id>/delete/", article_delete_view ,name="article-delete"),
]
