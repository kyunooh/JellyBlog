from django.contrib import admin

from .models import Category, Document

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','parent', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Document)