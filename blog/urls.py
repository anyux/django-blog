from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^detail/(?P<blog_id>[0-9]+)/$', views.detail,name='blog_detail'),
]
