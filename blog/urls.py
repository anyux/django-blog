from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^detail/(?P<blog_id>[0-9]+)/$', views.detail,name='blog_detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category,name='blog_category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag,name='blog_tag'),
    url(r'^search/$', views.search, name='blog_search'),
]
