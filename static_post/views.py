from django.shortcuts import render


def django_girls_july_seminar(request):
    return render(request, 'static_post/django_girls_july_seminar/index.html')