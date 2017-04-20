# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def details(request, my_args):
    # return HttpResponse("You're looking at my_args %s." % my_args)
    post = Article.objects.all()[int(my_args)]
    str = ('title = %s ,category = %s, date_time = %s,content = %s' % (post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)

def test(request):
    return render(request, 'index.html',{'current_time': datetime.now()})