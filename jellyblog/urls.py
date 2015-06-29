# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    # url 오른쪽의 주석은 각각 예시를 의미
    url(r'^$', views.index, name='index'),  # /
    url(r'^page/(?P<page>[0-9]+)/?$', views.index_with_page, name='index_with_page'), # /page/(page_number)
    url(r'^(?P<document_id>[0-9]+)/?$', views.detail, name='detail'),                 # /(document_id)
    url(r'^category/(?P<category_id>[0-9]+)/?$', views.category_detail, name='category_detail'), # /category/(category_id)
    url(r'^category/(?P<category_id>[0-9]+)/page/(?P<page>[0-9]+)/?$',
        views.category_with_page, name='category_with_page'), # /category/(category_id)/page/(page_number)
]