from django.db import models

# Create your models here.
class Madlib(models.Model):

    title = models.CharField(max_length=100, default='')
    blankCount = models.IntegerField(default=7)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    type3 = models.CharField(max_length=100)
    type4 = models.CharField(max_length=100)
    type5 = models.CharField(max_length=100)
    type6 = models.CharField(max_length=100)
    type7 = models.CharField(max_length=100)
    story = models.CharField(max_length=1000)