from django.db import models


# Create your models here.
from django.urls import reverse


class Purpose(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'course'

    def get_url(self):
        return reverse('newapp:department_by_course', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('newapp:deptcourcedetail',args=[self.course.slug,self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)




class Form(models.Model):
    name = models.CharField(max_length=124)
    dob= models.DateField(null=True,blank=True)
    age= models.IntegerField()
    gender=models.CharField(max_length=120)
    phn=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(blank=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    Purpose=models.ForeignKey(Purpose,on_delete=models.SET_NULL,null=True)
    debit=models.BooleanField("Debit",default=False)
    note_book=models.BooleanField("Note_Book",default=False)
    pen = models.BooleanField("Pen", default=False)
    exam_papper = models.BooleanField("Exam_papper", default=False)

    def __str__(self):
        return self.name