from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.children = []

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=20)



class Document(models.Model):
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = RichTextField()
    time = models.DateTimeField(auto_now=True)
    meta_tag = models.CharField(max_length=150)
    view_count = models.IntegerField(default=0, editable=False)
