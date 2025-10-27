from django.db import models

# Create your models here.
class Students(models.Model):
    id=models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)

    
