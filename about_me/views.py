from django.shortcuts import render

def index(request):
    return render('about_me/index.html')
