from django.db import models
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)
    description = models.TextField(blank=True)


    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('department_by_category',args=[self.slug])

    def __str__(self) -> str:
        return self.name    
    



class Course(models.Model)    :
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)
    department = models.ForeignKey(Department,related_name='children',on_delete=models.CASCADE,blank = True, null=True)
    


    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self) -> str:
        return self.name    
    
class Purpose(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class Choices(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description
    
class Person(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField( blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phoneno = models.IntegerField( blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    address = models.TextField( blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose,on_delete=models.SET_NULL, blank=True, null=True)
    Metirials_provide = models.ManyToManyField(Choices, blank=True)


    def __str__(self):
        return self.name








