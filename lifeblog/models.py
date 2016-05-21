from django.db import models
from django.db.models import Q


class Document(models.Model):
    # 문서 Model
    def __str__(self):
        return self.title

    id = models.AutoField(primary_key=True)
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
        return cls.objects.filter(
            (Q(title__icontains=query) | Q(content__icontains=query))
            & Q(public_doc=True))

