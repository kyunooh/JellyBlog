from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<page>[0-9]+)/$', views.index_with_page, name='index_with_page'),
    url(r'^(?P<document_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),
    url(r'^category/(?P<category_id>[0-9]+)/page/(?P<page>[0-9]+)/$', views.category_with_page, name='category_with_page'),
]