# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length = 100) #博客题目
    category = models.CharField(u'标签',max_length = 50, blank = True) #博客标签
    date_time = models.DateTimeField(u'信息发布日期',auto_now_add  = True) #博客日期
    content = models.TextField(u'信息简介',blank = True, null = True) #博客正文
    pub_time = models.DateTimeField(u'时间',null = True) #时间设置
    tel = models.IntegerField(u'电话',default=0)

    def __unicode__(self):
        return self.title

    class Meta: #按时间下降排序
        ordering = ['-date_time']


class side(models.Model):
    title = models.ForeignKey(Article)
    address = models.CharField(u'目的地',max_length = 100)
    price = models.IntegerField(u'路费',default=0)
    pub_time = models.DateTimeField(u'出发时间',null = True) #时间设置

