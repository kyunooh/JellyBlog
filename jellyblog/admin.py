from django.contrib import admin

from .models import Category, Document

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_id','category_parent_id', 'category_name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Document)