"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^blog/', include('blog.urls', namespace='blog')),
                  url(r'^latest/feed/$', LatestEntriesFeed(), name='rss'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error