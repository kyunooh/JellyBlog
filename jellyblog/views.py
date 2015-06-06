from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Document


def index(request):
    latest_document_list = Document.objects.order_by('-document_id')[:5]
    context = {'latest_document_list': latest_document_list}
    return render(request, 'jellyblog/index.html', context)


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'jellyblog/detail.html', {'document': document})


def category(request, category_id):
    return HttpResponse("Categoyr page %s." % category_id)

