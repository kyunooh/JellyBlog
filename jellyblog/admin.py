# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Document

class CategoryAdmin(admin.ModelAdmin):
	"""편의상 카테고리의 이름과, 상위카테고리만 표시"""
	list_display = ('name','parent' )


"""각각 카테고리와 문서 Model을 등록한다."""
admin.site.register(Category, CategoryAdmin)
admin.site.register(Document)