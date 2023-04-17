from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)


    def __str__(self):
        return '{}'.format(self.name)





