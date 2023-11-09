from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gmail = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    course_duration = models.CharField(max_length=50)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    course = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    

    