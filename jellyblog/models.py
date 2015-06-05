from django.db import models

# Create your models here.
class Document(models.Model):
	document_id = models.AutoField()
	category_id = models.ForeignKey(Category)
	document_title = models.CharField(max_length=100)
	document_content = models.TextField()
	document_time = models.DateTimeField()


class Category(models.Model):
	category_id = models.AutoField()
	category_parent_id = models.IntegerField()
	category_name = models.CharField(max_length=20)