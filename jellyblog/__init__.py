from .models import Category
from django.db import connection

is_empty = len(Category.objects.all()) == 0
if  is_empty:
    category = connection.cursor()
    category.execute('insert into jellyblog_category (name,parent_id) VALUES ("Home",1)')


