from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Article

from .models import Article, LikeArticle, DisLikeArticle
from ..core.utils import generate_navigation
from ..core.models import AnonymousUser


class NewsView(View):

    def get(self, request):
        articles = Article.objects.all()
        return render(
            request,
            'news/news.html',
            {
                'section': 'Новости',
                'articles': articles,
                'navigation': [
                    {
                        'title': 'Новости',
                        'url': reverse_lazy('news'),
                        'class': 'breadcrumb-item active',
                        'url_class': 'active'
                    }
                ]
            }
        )


class ArticleView(DetailView):
    model = Article
    template_name = 'news/article.html'
    context_object_name = 'article'


class UpdateLikeArticle(View):

    def post(self, request):
        user = None
        answer = int(request.POST.get('answer', None))
        anonim = False
        article = None

        if request.user:
            user = request.user
        else:
            sesid = request.COOKIES.get('sesid')
            if sesid:
                try:
                    user = AnonymousUser.objects.get(sesid=sesid)
                    anonim = True
                except Exception as e:
                    print(e)

        try:
            article = Article.objects.get(pk=int(request.POST.get('pk')))
        except Exception as e:
            print(e)

        us = {'user_anonim': user} if anonim else {'user': user}

        if user and article:
            dislike = DisLikeArticle.objects.filter(**us, article=article)
            like = LikeArticle.objects.filter(**us, article=article)

            if answer is not None and answer:
                if not like:
                    article.likes = 1 + article.likes
                    LikeArticle.objects.create(**us, article=article)
                if dislike:
                    if article.dis_likes:
                        article.dis_likes = article.dis_likes - 1
                    DisLikeArticle.objects.filter(**us, article=article).delete()
                article.save()
            if answer is not None and not answer:
                if not dislike:
                    article.dis_likes = 1 + article.dis_likes
                    DisLikeArticle.objects.create(**us, article=article)
                if like:
                    if article.likes:
                        article.likes = article.likes - 1
                    LikeArticle.objects.filter(**us, article=article).delete()
                article.save()

        data = {
            'like': article.likes,
            'dislike': article.dis_likes
        }
        return JsonResponse(data)
