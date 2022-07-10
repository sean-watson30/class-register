from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Class, Student, Photo

import uuid
import boto3



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def classes_index(request):
  classes = Class.objects.all()
  return render(request, 'classes/index.html', { 'classes': classes })
  # add more here later

def classes_detail(request, class_id):
  classes = Class.objects.get(id=class_id)
  students = Student.objects.exclude(id__in=classes.students.all().values_list('id'))
  # add more here later
  return render(request, 'classes/detail.html', {
    'class': classes, 'students': students
  })

# ________ Many-to-Many Associations __________
def assoc_student(request, class_id, student_id):
  Class.objects.get(id=class_id).students.add(student_id)
  return redirect('classes_detail', class_id=class_id)

def assoc_student_delete(request, class_id, student_id):
  Class.objects.get(id=class_id).students.remove(student_id)
  return redirect('classes_detail', class_id=class_id)

# ________ Sign Up Function __________
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid credentials. Please try login again.'
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)

# ________ Photo Handling __________


# ________ Class Declaration CRUD Functionality / Classes __________
class ClassCreate(CreateView):
  model = Class
  fields = ['title', 'studio', 'day_of_week', 'start_time', 'end_time', 'instructor']
  success_url = '/classes/'

class ClassUpdate(UpdateView):
  model = Class
  fields = ['title', 'studio', 'day_of_week', 'start_time', 'end_time', 'instructor']
  success_url = '/classes/'

class ClassDelete(DeleteView):
  model = Class
  success_url = '/classes/'

# ________ Class Declaration CRUD Functionality / Students __________

class StudentList(ListView):
  model = Student
  template_name = 'students/index.html'

class StudentDetail(DetailView):
  model = Student
  template_name = 'students/detail.html'

class StudentCreate(CreateView):
  model = Student
  fields = ['name', 'email', 'phone', 'age', 'address', 'city', 'state', 'zip']
  success_url = '/students/'

class StudentUpdate(UpdateView):
  model = Student
  fields = ['name', 'email', 'phone', 'age', 'address', 'city', 'state', 'zip']
  success_url = '/students/'

class StudentDelete(DeleteView):
  model = Student
  success_url = '/students/'

# ________ Class Declaration CRUD Functionality / Instructor __________

