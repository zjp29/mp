from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Dataset(models.Model):
    title = models.CharField(max_length=75)
    date_updated = models.DateField(auto_now=True)
    date_made = models.DateField(auto_now_add=True)
    renewal = models.DateField()
    summary = models.TextField(max_length = 300)
    detail = models.TextField()
    tags = TaggableManager()
    f = models.FileField()
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_made']

class URLs(models.Model):
    URL = models.URLField()
    desc = models.CharField(max_length=75)
    DS = models.ForeignKey(Dataset, on_delete=models.CASCADE)
