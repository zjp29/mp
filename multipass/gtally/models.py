from django.db import models

# Create your models here.

class Tally(models.Model):
    GAMES = (
        ('U','Uno'),
        ('P','Pandemic'),
        ('S','Scrabble'),
    )
    USERS = (
        ('M','Madelyne'),
        ('Z','Zach'),
    )
    game = models.CharField(max_length=1,choices=GAMES)
    winner = models.CharField(max_length=1,choices=USERS)
    w_score = models.IntegerField(null=True)
    l_score = models.IntegerField(null=True)
    date = models.DateField()

class Total(models.Model):
    Mt = models.IntegerField()
    Zt = models.IntegerField()
    Ot = models.IntegerField()