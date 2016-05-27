from django.conf.urls import url

from .views import DocumentList, DocumentDetail

urlpatterns = [
    url(r'^$', DocumentList.as_view(), name="lifeblog-index"),
    url(r'^(?P<slug>[-\w]+)/$',
        DocumentDetail.as_view(), name='lifdeblog-document-detail'),
]
