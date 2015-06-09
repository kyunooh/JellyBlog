from django.shortcuts import render, get_object_or_404
from .models import Category, Document


category_list = Category.objects.all()

def index(request):
    latest_document_list = Document.objects.order_by('-document_id')[:5]
    context = {'latest_document_list': latest_document_list,'category_list' : category_list }
    return render(request, 'jellyblog/index.html', context)


def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'jellyblog/detail.html', {'document': document, 'category_list': category_list})


def category(request, category_id):
    document = get_object_or_404(Category, pk=category_id)
    return render(request, 'jellyblog/category.html',{'category_list':category_list})


