from django.db import models

# Create your models here.

class Entry(models.Model):
    time = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    cat = models.CharField(max_length=50)
    blogslug = models.SlugField()
    blog = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='blog_photos/')

#class Zcss(models.Model):
