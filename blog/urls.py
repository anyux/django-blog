from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^detail/(?P<blog_id>[1-9]+)/$', views.detail,name='blog_detail'),
]
