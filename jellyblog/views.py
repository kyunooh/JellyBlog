from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from jellyblog.forms import SearchForm
from .models import Category, Document
from htmlmin.decorators import minified_response
from .util import get_page_number_range, get_documents


def init_category():
    Category.init_category()


@minified_response
def home(request):
    init_category()
    return render(request, 'jellyblog/home.html')


@minified_response
def index(request):
    return index_with_page(request, 1)


@minified_response
def index_with_page(request, page):
    document_list = Document.objects.filter(public_doc=True).order_by('-id')
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {
        'documents': documents,
        'category_list': Category.sorted_category(),
        'page_range': get_page_number_range(
            paginator, documents
        ),
        'test': settings.TEST

    }
    return render(request, 'jellyblog/index.html', context)


@minified_response
def category_detail(request, category_id):
    return category_with_page(request, category_id, 1)


@minified_response
def category_with_page(request, category_id, page):
    selected_category = Category.objects.get(id=category_id)
    document_list = []
    if selected_category.parent.id == 1:
        # 카테고리가 상위 카테고리인지 아닌지를 판별 후,
        # 상위 카테고리일 경우엔 하위 카테고리의 문서 리스트를 추가함
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
        'category_list': Category.sorted_category(),
        'category_id': category_id,
        'page_range': get_page_number_range(
            paginator, documents),
        'category_name': selected_category.name,
        'test': settings.TEST
    }
    return render(request, 'jellyblog/category.html', context)


@minified_response
def search_documents(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        documents = Document.search_document(form.cleaned_data['search_query'])
        context = {
            'documents' : documents,
            'category_list' : Category.sorted_category()
        }
        return render(request, 'jellyblog/search_result.html', context)
    else:
        return render(request, 'jellyblog/search_result.html')


@minified_response
def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.read()
    return render(request, 'jellyblog/detail.html',
                  {'document': document,
                   'category_list': Category.sorted_category(),
                   'test': settings.TEST}
                  )