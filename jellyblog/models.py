from django.db import models


class Category(models.Model):
	def __str__(self):
		return self.category_name

	category_id = models.AutoField(primary_key=True)
	category_parent_id = models.IntegerField(null=True)
	category_name = models.CharField(max_length=20)


class Document(models.Model):
	def __str__(self):
		return self.document_title

	document_id = models.AutoField(primary_key=True)
	category = models.ForeignKey(Category)
	document_title = models.CharField(max_length=100)
	document_content = models.TextField()
	document_time = models.DateTimeField()