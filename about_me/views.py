from django.conf import settings
from django.shortcuts import render
from .models import Message

def index(request):
    if request.method == "POST":
        message = Message()
        message.name = request.POST['name']
        message.email = request.POST['email']
        message.content = request.POST['content']
        message.save()
    return render(request, 'about_me/index.html', {'test': settings.TEST})
