from django.conf.urls import url

from static_post import views

urlpatterns = [
    url(r'^django-girls-july-seminar$', views.django_girls_july_seminar, name='django_girls_july_seminar'),
]
