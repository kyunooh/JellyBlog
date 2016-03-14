# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
    # 카테고리 Model
    # 모든 카테고리는 상위 카테고리(parent)를 가지고 있다. (자기 참조)
    # parent의 id가 1일 경우 상위 카테고리,
    # 1이 아닌 경우 하위 카테고리로 분류한다.
    # (참고로 1은 사이트 최초 접속시 생성되며 Home 값을 가진다.
    # 상세내용은 views.py의 상단부분과 sorted_category()함수 참고)
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        # 상위 카테고리에서 하위 카테고리 리스트를 가지기 위해
        # 초기화시 children 리스트를 추가, (상세내용은 views.py의 sorted_category()함수 참고
        #
        # 생성자에 list를 선언하지않고 Category에 바로 선언할 경우
        # 모든 카테고리가 list를 공유하는 이슈(자바상의 static 변수와 같이 동작한다)가 발생하기 때문에 생성자에 선언
        super(Category, self).__init__(*args, **kwargs)
        self.children = []

    def __str__(self):
        return self.name


    @classmethod
    def sorted_category(cls):
        # 카테고리를 정렬하기 위한 함수,
        # 상위 카테고리는 남겨두고, 하위 카테고리의 경우 상위 카테고리(parent)의 자식(children)으로 집어넣는다.
        # 추후 리팩토링 예정
        # 전체 카테고리를 불러온뒤 리스트로 변환한다.
        return_category = list(cls.objects.all())
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

    


@python_2_unicode_compatible
class Document(models.Model):
    # 문서 Model
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = RichTextField()
    time = models.DateTimeField(auto_now_add=True)
    meta_tag = models.CharField(max_length=150)
    view_count = models.IntegerField(default=0, editable=False)
    public_doc = models.BooleanField()
    update_time = models.DateTimeField(auto_now=True)

    def read(self):
        self.view_count += 1
        self.save()

    @models.permalink
    def get_absolute_url(self):
        return 'detail', (), {'document_id': self.id}

@python_2_unicode_compatible
class Note(models.Model):
    # 노트 Model
    def __str__(self):
        return self.content

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
