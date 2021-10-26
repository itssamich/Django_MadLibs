from django.db import models

# Create your models here.
class Madlib(models.Model):

    title = models.CharField(max_length=100, default='')
    blankCount = models.IntegerField(default=7)
    type1 = models.CharField(max_length=100, default='')
    type2 = models.CharField(max_length=100, default='')
    type3 = models.CharField(max_length=100, default='')
    type4 = models.CharField(max_length=100, default='')
    type5 = models.CharField(max_length=100, default='')
    type6 = models.CharField(max_length=100, default='')
    type7 = models.CharField(max_length=100, default='')
    type8 = models.CharField(max_length=100, default='')
    type9 = models.CharField(max_length=100, default='')
    type10 = models.CharField(max_length=100, default='')
