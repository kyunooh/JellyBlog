# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    #카테고리 Model
    #모든 카테고리는 상위 카테고리(parent)를 가지고 있다. (자기 참조)
    #parent의 id가 1일 경우 상위 카테고리,
    #1이 아닌 경우 하위 카테고리로 분류한다.
    #(참고로 1은 사이트 최초 접속시 생성되며 Home 값을 가진다.
    #상세내용은 views.py의 상단부분과 sorted_category()함수 참고)

    def __init__(self, *args, **kwargs):
        #상위 카테고리에서 하위 카테고리 리스트를 가지기 위해
        #초기화시 children 리스트를 추가, (상세내용은 views.py의 sorted_category()함수 참고
        #    
        #생성자에 list를 선언하지않고 Category에 바로 선언할 경우
        #모든 카테고리가 list를 공유하는 이슈(자바상의 static 변수와 같이 동작한다)가 발생하기 때문에 생성자에 선언
        super(Category, self).__init__(*args, **kwargs)
        self.children = []

    def __str__(self):
        #객체 참조시 카테고리의 이름을 리턴하게끔 수정
        return self.name.encode('utf-8')

    id = models.AutoField(primary_key=True) # 카테고리 id (auto_increment)
    parent = models.ForeignKey('self')      # 상위 카테고리 (자기 참조)
    name = models.CharField(max_length=20)  # 이름



class Document(models.Model):
    #문서 Model
    def __str__(self):
        #객체 참조시 문서의 제목을 리턴하게끔 수정
        return self.title.encode('utf-8')

    id = models.AutoField(primary_key=True)     # 문서 id (auto_increment)
    category = models.ForeignKey(Category)      # 카테고리 id (Category 참조)
    title = models.CharField(max_length=100)    # 제목
    content = RichTextField()                   # 내용, 편집기인 ckeditor를 사용하기 위해 RichTextField()를 사용한다.
    time = models.DateTimeField(auto_now_add=True)  # 작성시간 (자동입력)
    update_time = models.DateTimeField(auto_now=True) #최종 수정 시간(자동 입력)
    meta_tag = models.CharField(max_length=150) # 검색 최적화를 위한 메타 태그
    view_count = models.IntegerField(default=0, editable=False) # 조회수
    public_doc = models.BooleanField() # 공개글 여부


class Note(models.Model):
    #노트 Model
    def __str__(self):
        #객체 참조시 문서의 제목을 리턴하게끔 수정
        return self.title.encode('utf-8')

    id = models.AutoField(primary_key=True)         # 노트 id(auto_increment)
    content = models.CharField(max_length=300)      # 노트 내용
    time = models.DateTimeField(auto_now_add=True)  # 작성시간 (자동입력)
    update_time = models.DateTimeField(auto_now=True) #최종 수정 시간(자동 입력)