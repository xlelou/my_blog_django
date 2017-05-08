# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article,side

# Register your models here.

class sideInline(admin.TabularInline):
    model = side
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    list_filter = ('pub_time',)
    fieldsets = (
        ['Main',{
            'fields':('title','content','tel'),
        }],
    )
    inlines = [sideInline]

admin.site.register(Article, ArticleAdmin)