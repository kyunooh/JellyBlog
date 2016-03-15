from django.shortcuts import render


def index(request):
    return render(request, 'about_me/not_ready.html')
