#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Article, Comment, get_article
from itreactor.settings import PAGINATION_ARTICLES_ON_PAGE, PAGINATION_LIST_RANGE, \
    TEMPLATE_BLOG_LIST, TEMPLATE_BLOG_DETAIL

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import User
from blog.models import Tips

# Create your views here.
from django.template.context_processors import csrf


@csrf_protect
def comment(request, articles_id):
    response = True

    articles = Comment.objects.create(
            author=request.POST[u'form-articles-reply-name'],
            email=request.POST[u'form-articles-reply-email'],
            articles_id=articles_id,
            message=u'<p>%s</p>' % request.POST[u'form-articles-reply-message'],
        )
    try:
        articles.reply_id = request.POST[u'form-articles-reply-comment']
    except articles.DoesNotExist:
        articles.reply_id = None
    articles.save()

    return JsonResponse(response, safe=False)


@csrf_protect
def blog_detail(request, articles_id):
    context = {}
    context.update(csrf(request))
    if request.user.is_authenticated:
        # context[u'profile'] = auth.get_user(request).photo
        context[u'reply_name'] = auth.get_user(request).get_short_name
        context[u'reply_email'] = auth.get_user(request).email
        context[u'photo'] = User.objects.get(is_superuser=True).photo

    #context[u'menus'] = menus()
    #context[u'menu_default'] = MENU_DEFAULT
    context[u'result'] = True
    articles = []
    try:
        articles = Article.objects.get(id=articles_id)
    except Article.DoesNotExist:
        context[u'result'] = False
    context[u'articles'] = articles
    _comments = Comment.objects.filter(articles_id=articles_id, allowed=True)
    # добавка чтобы реплика была адресно
    for _comment in _comments:
        if _comment.reply:
            _comment.message = u"%s<a href='#%s'>%s</a>, %s" \
                               % (_comment.message[:3], _comment.reply.id, _comment.reply.author, _comment.message[3:])

    context[u'comments'] = _comments
    return render(request, TEMPLATE_BLOG_DETAIL, context)


@csrf_protect
def blog_list(request, tag_id=None, page=None):
    context = {}
    context.update(csrf(request))
    paginator = Paginator(get_article(tag_id), PAGINATION_ARTICLES_ON_PAGE)

    try:
        articles_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles_list = paginator.page(paginator.num_pages)

    if paginator.num_pages > PAGINATION_LIST_RANGE * 2 + 1:
        list_start = articles_list.number - PAGINATION_LIST_RANGE
        list_end = articles_list.number + PAGINATION_LIST_RANGE

        if list_start < 1:
            list_start = 1
            list_end = PAGINATION_LIST_RANGE * 2 + 1

        if list_end > paginator.num_pages:
            list_start = paginator.num_pages - PAGINATION_LIST_RANGE * 2
            list_end = paginator.num_pages

        articles_list.list_range = range(list_start, list_end + 1)
    else:
        articles_list.list_range = range(1, paginator.num_pages + 1)

    if request.user.is_authenticated:
        context['username'] = auth.get_user(request).username
        context['profile'] = auth.get_user(request).photo
        context['tags'] = Tips.objects.all()
        context['tag_id'] = int(tag_id) if tag_id else None
    context['result'] = True
    context['articles_list'] = articles_list
    context['articles_widget'] = Article.objects.all()[:3]
    return render(request, TEMPLATE_BLOG_LIST, context)
