from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<document_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^category/(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),
]