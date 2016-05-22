from django.conf.urls import url, include
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.sitemaps.views import sitemap

from jellyblog import views

from .feeds import LatestFeed, AllPublickFeed
from .sitemaps import BlogSitemap
from .serializer import router

sitemaps = {
    'blog': BlogSitemap,
}


urlpatterns = [
    # url 오른쪽의 주석은 각각 예시를 의미
    url(r'^$', views.home, name='home'),
    # blog의 첫 페이지를 보여준다.
    url(r'^index/$', views.index, name='blog_index'),
    # 검색 결과를 보여준다.
    url(r'^search/$', views.search_documents, name='search_documents'),
    # /page/(page_number)
    url(r'^page/(?P<page>[0-9]+)/?$',
        views.index_with_page, name='index_with_page'),

    # /(document_id)
    url(r'^(?P<document_id>[0-9]+)/?$', views.detail, name='detail'),

    # /category/(category_id)
    url(r'^category/(?P<category_id>[0-9]+)/?$',
        views.category_detail, name='category_detail'),

    # /category/(category_id)/page/(page_number)
    url(r'^category/(?P<category_id>[0-9]+)/page/(?P<page>[0-9]+)/?$',
        views.category_with_page, name='category_with_page'),

    # google chrome favicon fix
    url(r'^favicon.ico/$',
        lambda x: HttpResponseRedirect(settings.STATIC_URL+'ico/favicon.ico')),

    url(r'^latest/feed/$', LatestFeed()),

    url(r'^public/feed/$', AllPublickFeed()),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^api/', include(router.urls))
]
