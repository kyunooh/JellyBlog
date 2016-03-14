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
        category.execute('INSERT INTO jellyblog_category \
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


# 성능을 위해 카테고리 리스트의 경우 캐싱해서 사용
categoryList = Category.sorted_category()