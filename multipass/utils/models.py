from django.db import models

# Create your models here.
# things I want to keep track of for my own personal usage



class Exercise(models.Model):
    time = models.DateField(verbose_name="Date Recorded")
    daycat = models.CharField(max_length=100, verbose_name="Muscles Worked")
    time = models.TimeField()
    detail = models.CharField(max_length=500)

class Games(model.Model):
    pass

