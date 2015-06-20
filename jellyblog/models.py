from django.db import models
from pip.cmdoptions import editable


class Category(models.Model):
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.children = []

    def __str__(self):
        return str(self.id)

    id = models.AutoField(primary_key=True)
    parent = models.IntegerField()
    name = models.CharField(max_length=20)
    is_child = models.BooleanField()


class Document(models.Model):
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0, editable=False)
