from django.conf.urls import url

from .views import DocumentList

urlpatterns = [
    url(r'^$', DocumentList.as_view(), name="lifeblog-index")
]