from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=8)
    first_greet = models.CharField(max_length=50)
    middle_greet = models.TextField()
    last_greet = models.CharField(max_length=150)
    overlay_image = models.ImageField()
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)

class About(models.Model):
    first_head = models.CharField(max_length=15)
    second_head = models.CharField(max_length=50)
    first_content = models.TextField()
    second_content = models.TextField()
    image = models.ImageField()
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)

class Usually(models.Model):
    first_icon = models.CharField(max_length=50)
    second_icon = models.CharField(max_length=50)
    third_icon = models.CharField(max_length=50)
    first_head = models.CharField(max_length=30)
    second_head = models.CharField(max_length=30)
    thrid_head = models.CharField(max_length=30)
    first_content = models.TextField()
    second_content = models.TextField()
    third_content = models.TextField()
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)

class PortFolio(models.Model):
    first_head = models.CharField(max_length=30)
    first_content = models.TextField()
    second_content = models.TextField()
    third_content = models.TextField()
    fourth_content = models.TextField()
    fifth_content = models.TextField()
    sixth_content = models.TextField()
    seventh_content = models.TextField()
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)


class ETC(models.Model):
    first_content = models.TextField()
    second_content = models.TextField()
    thrid_content = models.TextField()
    fourth_content = models.TextField()
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)

class Contact(models.Model):
    content = models.TextField()
    facebook = models.CharField(max_length=30)
    github = models.CharField(max_length=30)
    google = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    email = models.CharField(max_length=70)
    created_datetime = models.TimeField(auto_now_add=True)
    updated_datetime = models.TimeField(auto_now=True)
