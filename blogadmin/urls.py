"""blogadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from jellyblog import urls as blog_urls
from about_me import views as about_me_views

urlpatterns = [
    # admin에 접속하기 위한 url
    url(r'^admin/', include(admin.site.urls)),

    # about me 접속 url
    url(r'^about_me/', about_me_views.index, name="about_me"),
    # jellyblog에 접속하기 위한 url
    url(r'^', include(blog_urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
