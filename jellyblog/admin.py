from django.contrib import admin

from jellyblog import models as jelly_model
from lifeblog import models as life_model


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


# 각각 카테고리와 문서 Model을 등록한다.
admin.site.register(jelly_model.Category, CategoryAdmin)
admin.site.register(jelly_model.Document)
admin.site.register(jelly_model.Note)
admin.site.register(life_model.Document)
