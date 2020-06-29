from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment

from django.urls import reverse
def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})
def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('No Article.')
    latest_comment_list = a.comment_set.order_by('-id')[:5]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('No Article.')
    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['comment'])

    return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)))