# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Document, Note
from htmlmin.decorators import minified_response
from .util import get_page_number_range, get_documents, \
    categoryList

Category.init_category()


def home(request):
    categoryList = Category.sorted_category()
    return render(request, 'jellyblog/home.html')


def index(request):
    return index_with_page(request, 1)


@minified_response
def index_with_page(request, page):
    """
    모든 문서를 가져와 리스트형태로 바꾼뒤 페이지네이션하여
    해당 페이지의 문서 리스트를 반환한다.
    """
    document_list = Document.objects.all().filter(public_doc=True).order_by('-id')
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
    """
    선택된 카테고리에 대한 문서를 가져온뒤 페이지네이하여
    해당 페이지의 문서리스트를 반환한다.
    """
    selectedCategory = Category.objects.get(id=category_id)
    document_list = []
    if (selectedCategory.parent.id == 1):
        # 카테고리가 상위 카테고리인지 아닌지를 판별 후, 상위 카테고리일 경우엔 하위 카테고리의 문서 리스트를 추가함
        children = Category.objects.all().filter(parent=selectedCategory.id)
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
        'category_name': selectedCategory.name,
    }
    return render(request, 'jellyblog/category.html', context)


@minified_response
def detail(request, document_id):
    """
    document_id에 해당하는 문서를 가져오고, 해당 문서가 존재하지 않을경우 404페이지를 반환한다.
    함수를 호출할때 마다 해당 문서의 조회수를 1올려주고 반환한다.
    """
    document = get_object_or_404(Document, pk=document_id)
    document.read()
    return render(request, 'jellyblog/detail.html',
                  {'document': document, 'category_list': categoryList})


def get_notes(request):
    return HttpResponse(serializers.serialize('json', Note.objects.all()))
