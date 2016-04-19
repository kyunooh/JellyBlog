# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Document
from htmlmin.decorators import minified_response
from .util import get_page_number_range, get_documents, \
    categoryList


def home(request):
    Category.init_category()
    return render(request, 'jellyblog/home.html')


def index(request):
    return index_with_page(request, 1)


@minified_response
def index_with_page(request, page):
    document_list = Document.objects.filter(public_doc=True).order_by('-id')
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {
        'documents': documents,
        'category_list': categoryList,
        'page_range': get_page_number_range(
            paginator, documents
        )
    }
    return render(request, 'jellyblog/index.html', context)


def category_detail(request, category_id):
    return category_with_page(request, category_id, 1)


@minified_response
def category_with_page(request, category_id, page):
    selected_category = Category.objects.get(id=category_id)
    document_list = []
    if selected_category.parent.id == 1:
        # 카테고리가 상위 카테고리인지 아닌지를 판별 후, 상위 카테고리일 경우엔 하위 카테고리의 문서 리스트를 추가함
        children = Category.objects.all().filter(parent=selected_category.id)
        for child in children:
            document_list += Document.objects.all() \
                .filter(category_id=child.id, public_doc=True)
    document_list += Document.objects.all().filter(
        category=category_id, public_doc=True)
    document_list.sort(key=lambda x: x.pk, reverse=True)
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {
        'documents': documents,
        'category_list': categoryList,
        'category_id': category_id,
        'page_range': get_page_number_range(
            paginator, documents),
        'category_name': selected_category.name,
    }
    return render(request, 'jellyblog/category.html', context)


@minified_response
def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.read()
    return render(request, 'jellyblog/detail.html',
                  {'document': document, 'category_list': categoryList})

