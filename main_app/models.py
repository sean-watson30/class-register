from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

DAYS = (
  ('Mon', 'Monday'),
  ('Tue', 'Tuesday'),
  ('Wed', 'Wednesday'),
  ('Thu', 'Thursday'),
  ('Fri', 'Friday'),
  ('Sat', 'Saturday'),
  ('Sun', 'Sunday'),
)

class Student(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=13)
  age = models.IntegerField()
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=150)
  state = models.CharField(max_length=2)
  zip = models.CharField(max_length=5)
  def __str__(self):
    return f"{self.name}"
  def get_absolute_url(self):
    return reverse('students_detail', kwargs={'pk': self.id})

class Instructor(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=13)
  # classes = models.ManyToManyField(Class, related_name='classes')
  def __str__(self):
    return f"{self.name}"
  def get_absolute_url(self):
    return reverse('instructors_detail', kwargs={'pk': self.id})

class Class(models.Model):
  title = models.CharField(max_length=200)
  studio = models.IntegerField()
  # day_of_week = models.CharField(max_length=25)
  day_of_week = models.CharField(
    max_length=3, choices=DAYS, default=DAYS[0][0]
  )
  start_time = models.CharField(max_length=10)
  end_time = models.CharField(max_length=10)
  instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  # instructors = models.CharField(max_length=150)
  # instructors = models.ManyToManyField(Instructor, related_name='classes')
  students = models.ManyToManyField(Student, related_name='classes')
  def __str__(self):
    return f"{self.title}"
  def get_absolute_url(self):
    return reverse('classes_detail', kwargs={'pk': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=200)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  # instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
  def __str__(self):
    return f"photo for student_id: {self.student_id} @{self.url}"