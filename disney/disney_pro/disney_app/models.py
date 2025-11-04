from django.db import models

# Create your models here.
class Coders(models.Model):
    name=models.CharField(max_length=50, null=True)
    age=models.IntegerField()