from django.conf.urls import *
# from views import home
# from views import detail
from . import views
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    # url(r'^detail/$',home,name='detail'),
    url(r'^archives/$',  views.archives, name = 'archives'),
    url(r'^aboutme/$',  views.about_me, name = 'aboutme'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^search/$',views.blog_search, name = 'search'),
]