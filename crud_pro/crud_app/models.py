from django.db import models

# Create your models here.
class Faculty(models.Model):
    id=models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    branch=models.CharField(max_length=40)
    def __str__(self):
        return self.f_name + " " + self.l_name
