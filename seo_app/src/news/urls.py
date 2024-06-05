from django.urls import path
from .views import NewsView, ArticleView, UpdateLikeArticle


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('article/<slug:slug>/', ArticleView.as_view(), name='article'),
    path('update_like/', UpdateLikeArticle.as_view(), name='update_like_article')
]