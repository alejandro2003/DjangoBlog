
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),

]
