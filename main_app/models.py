from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
  name = models.CharField(max_length=150)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=12)

class Student(models.Model):
  name = models.CharField(max_length=150)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=12)
  age = models.CharField(max_length=2)
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=150)
  state = models.CharField(max_length=2)
  zip = models.CharField(max_length=5)
  # classes = models.ManyToManyField(Class)
  def __str__(self):
    return f"{self.name}"
  def get_absolute_url(self):
    return reverse('students_detail', kwargs={'pk': self.id})


class Class(models.Model):
  title = models.CharField(max_length=200)
  studio = models.CharField(max_length=1)
  day_of_week = models.CharField(max_length=25)
  start_time = models.CharField(max_length=10)
  end_time = models.CharField(max_length=10)
  instructor = models.ForeignKey(User, on_delete=models.CASCADE)
  students = models.ManyToManyField(Student)
  def __str__(self):
    return f"{self.title}"
  def get_absolute_url(self):
    return reverse('classes_detail', kwargs={'pk': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  def __str__(self):
    return "this is a photo."