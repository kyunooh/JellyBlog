from django.contrib import admin

from .models import Category, Document, Note


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


# 각각 카테고리와 문서 Model을 등록한다.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Document)
admin.site.register(Note)
