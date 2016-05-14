from django.db import models, connection
from django.db.models import Q


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=20)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.children = []

    def __str__(self):
        return self.name

    @classmethod
    def sorted_category(cls):
        return_category = list(cls.objects.all())
        childList = []
        for category in return_category:
            if (category.parent.id == 1):
                continue
            else:
                parent_index = return_category.index(category.parent)
                return_category[parent_index].children.append(category)
                childList.append(category)

        for child in childList:
            return_category.remove(child)

        return return_category

    @classmethod
    def init_category(cls):
        is_empty = cls.objects.count() == 0
        if is_empty:
            with connection.cursor() as cs:
                cs.execute('INSERT INTO jellyblog_category (name, parent_id) VALUES ("Home", 1)')


class Document(models.Model):
    # 문서 Model
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
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

    @classmethod
    def search_document(cls, query):
        if len(query) == 0:
            return None
        return cls.objects.filter(Q(title__icontains=query)
                                  | Q(content__icontains=query)
                                  & Q(public_doc=True))


class Note(models.Model):
    # 노트 Model
    def __str__(self):
        return self.content

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
