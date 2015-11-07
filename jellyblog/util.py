# -*- coding: utf-8 -*-
from .models import Category
from django.db import connection
from django.core.paginator import EmptyPage, PageNotAnInteger

"""
최초 접속시 Home 카테고리를 생성하기 위함.

카테고리가 존재여부를 확인후 존재하지 않을시
Home 카테고리를 생성하도록 쿼리를 실행한다.
"""


def init_category():
    is_empty = len(Category.objects.all()) == 0
    if is_empty:
        category = connection.cursor()
        category.execute('insert into jellyblog_category \
             (name, parent_id) VALUES ("Home", 1)')

        
def get_page_number_range(paginator, page):
    # 페이지네이션의 범위를 반환해주는 함수
    # 총 페이지 수가 10개 이하일 경우 1 ~ (총 페이지 수) 보여줌
    if (paginator.num_pages < 11): 
        return range(1, paginator.num_pages + 1)

    # 선택된 페이지번호가 6보다 크고
    elif (page.number > 6): 
        if (page.number + 4 < paginator.num_pages):
            # {선택된 페이지번호 + 4} 페이지가 더 있을 경우 (현재 페이지 - 5) ~ (현재 페이지 + 4)까지 보여줌
            return range(page.number - 5, page.number + 5)
            # {선택된 페이지번호 + 4} 보단 적을 경우 (현재 페이지 - 5) ~ (총 페이지 수)까지 보여줌
        else:
            return range(page.number - 5, paginator.num_pages + 1)
    # 나머지 경우에 대해선 1 ~ 10까지 보여준다.
    else: 
        return range(1, 11)


def get_documents(paginator, page):
    # 각 페이지에 해당하는 문서들을 가져오는 함수
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)
    return documents


def sorted_category():
    # 카테고리를 정렬하기 위한 함수,
    # 상위 카테고리는 남겨두고, 하위 카테고리의 경우 상위 카테고리(parent)의 자식(children)으로 집어넣는다.
    # 추후 리팩토링 예정
    # 전체 카테고리를 불러온뒤 리스트로 변환한다.
    return_category = list(Category.objects.all())
    childList = []     # 하위 카테고리를 담을 리스트 생성
    for category in return_category:
        # 전체 카테고리 리스트를 반복 하면서 상위 카테고리의 경우(parent == 1) 아무처리도 하지 않는다.
        if (category.parent.id == 1):
            continue
        else:
            # 상위 카테고리 위치를 반환한다.
            parent_index = return_category.index(category.parent)
            # 상위 카테고리의 children 리스트에 요소추가
            return_category[parent_index].children.append(category)
            # 하위 카테고리 리스트에 담음
            childList.append(category)

    # 카테고리 리스트에서 하위 카테고리의 값들은 삭제
    for child in childList:
        return_category.remove(child)

    return return_category

# 성능을 위해 카테고리 리스트의 경우 캐싱해서 사용
categoryList = sorted_category()
