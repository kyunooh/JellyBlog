from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Home, About, Usually, PortFolio, ETC, Contact


def index(request):
    try:
        home = Home.objects.latest('updated_datetime')
        about = About.objects.latest('updated_datetime')
        usually = Usually.objects.latest('updated_datetime')
        portfolio = PortFolio.objects.latest('updated_datetime')
        etc = ETC.objects.latest('updated_datetime')
        contact = Contact.objects.latest('updated_datetime')

        return render(request, 'about_me/index.html', {
                                            "home" : home,
                                            "about" : about,
                                            "usually" : usually,
                                            "portfolio" : portfolio,
                                            "etc" : etc,
                                            "contact" : contact
                                })
    except ObjectDoesNotExist:
        return render(request, 'about_me/not_ready.html')
