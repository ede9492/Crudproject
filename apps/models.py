from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=False)
    age=models.CharField(max_length=50,blank=False)
    gender=models.CharField(max_length=50,blank=False)
    
    def __str__(self):
        return self.name