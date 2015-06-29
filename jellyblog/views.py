# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Document
from django.db import connection
from htmlmin.decorators import minified_response

"""
최초 접속시 Home 카테고리를 생성하기 위함.

카테고리가 존재여부를 확인후 존재하지 않을시
Home 카테고리를 생성하도록 쿼리를 실행한다.
코드가 굉장히 지저분 해지고, 전역변수 사용으로 인해 추후 리팩토링 필요
"""
is_empty = len(Category.objects.all()) == 0
if is_empty:
    category = connection.cursor()
    category.execute('insert into jellyblog_category (name,parent_id) VALUES ("Home",1)')



def sorted_category():
    """
    카테고리를 정렬하기 위한 함수,
    상위 카테고리는 남겨두고, 하위 카테고리의 경우 상위 카테고리(parent)의 자식(children)으로 집어넣는다.

    추후 리팩토링 예정
    """
    return_category = list(Category.objects.all()) # 전체 카테고리를 불러온뒤 리스트로 변환한다.
    childList = []     # 하위 카테고리를 담을 리스트 생성
    for category in return_category:
        # 전체 카테고리 리스트를 반복 하면서 상위 카테고리의 경우(parent == 1) 아무처리도 하지 않는다.
        if (category.parent.id == 1):
            continue
        else:
            parent_index = return_category.index(category.parent)   # 상위 카테고리 위치를 반환한다.
            return_category[parent_index].children.append(category) # 상위 카테고리의 children 리스트에 요소추가
            childList.append(category) # 하위 카테고리 리스트에 담음

    for child in childList: # 카테고리 리스트에서 하위 카테고리의 값들은 삭제
        return_category.remove(child)

    return return_category


categoryList = sorted_category() # 성능을 위해 카테고리 리스트의 경우 캐싱해서 사용


def get_documents(paginator, page):
    #각 페이지에 해당하는 문서들을 가져오는 함수
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)
    return documents


def get_page_number_range(paginator, page):
    #페이지네이션의 범위를 반환해주는 함수
    if (paginator.num_pages < 11): # 총 페이지 수가 10개 이하일 경우 1 ~ (총 페이지 수) 보여줌
        return range(1, paginator.num_pages + 1)

    elif (page.number > 6): # 선택된 페이지번호가 6보다 크고
        if (page.number + 4 < paginator.num_pages):
            # {선택된 페이지번호 + 4} 페이지가 더 있을 경우 (현재 페이지 - 5) ~ (현재 페이지 + 4)까지 보여줌
            return range(page.number - 5, page.number + 5)
            # {선택된 페이지번호 + 4} 보단 적을 경우 (현재 페이지 - 5) ~ (총 페이지 수)까지 보여줌
        else:
            return range(page.number - 5, paginator.num_pages + 1)

    else: # 나머지 경우에 대해선 1 ~ 10까지 보여준다.
        return range(1, 11)

def index(request):
    return index_with_page(request,1)

@minified_response
def index_with_page(request, page):
    """
    모든 문서를 가져와 리스트형태로 바꾼뒤 페이지네이션하여
    해당 페이지의 문서 리스트를 반환한다.
    """
    document_list = list(Document.objects.all())
    document_list.reverse()
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {'documents': documents, 'category_list': categoryList, 'page_range': get_page_number_range(
        paginator, documents)}
    return render(request, 'jellyblog/index.html', context)


def category_detail(request, category_id):
    return category_with_page(request,category_id,1)

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
            document_list += Document.objects.all().filter(category_id=child.id)
    document_list += Document.objects.all().filter(category=category_id)
    document_list.sort(key=id, reverse=True)
    paginator = Paginator(document_list, 4)
    documents = get_documents(paginator, page)
    context = {'documents': documents, 'category_list': categoryList, 'category_id': category_id,
               'page_range': get_page_number_range(paginator, documents),'category_name' : selectedCategory.name}
    return render(request, 'jellyblog/category.html', context)

@minified_response
def detail(request, document_id):
    """
    document_id에 해당하는 문서를 가져오고, 해당 문서가 존재하지 않을경우 404페이지를 반환한다.
    함수를 호출할때 마다 해당 문서의 조회수를 1올려주고 반환한다.
    """
    document = get_object_or_404(Document, pk=document_id)
    document.view_count += 1
    document.save()
    return render(request, 'jellyblog/detail.html', {'document': document, 'category_list': categoryList})
