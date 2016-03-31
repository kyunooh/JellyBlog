from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=150)
    content = models.TextField(null=False)

    def __str__(self):
        return self.name
