from django.shortcuts import render, redirect

# from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Class, Student, Instructor, Photo

import uuid
import boto3



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def classes_index(request):
  classes = Class.objects.all()
  instructor = Instructor.objects.all()
  return render(request, 'classes/index.html', { 'classes': classes, 'instructor': instructor })
  # add more here later

@login_required
def classes_detail(request, class_id):
  classes = Class.objects.get(id=class_id)
  students = Student.objects.exclude(id__in=classes.students.all().values_list('id'))
  # instructor = Instructor.objects.exclude(id__in=classes.instructor.all().values_list('id'))
  instructor = Instructor.objects.all()
  return render(request, 'classes/detail.html', {
    'class': classes, 'students': students, 'instructor': instructor
  })

@login_required
def students_index(request):
  students = Student.objects.all()
  return render(request, 'students/index.html', { 'students': students })

@login_required
def students_detail(request, student_id):
  student = Student.objects.get(id=student_id)
  classes = Class.objects.exclude(id__in=student.classes.all().values_list('id'))
  return render(request, 'students/detail.html', {
    'student': student, 'classes': classes 
  })

@login_required
def instructors_index(request):
  instructors = Instructor.objects.all()
  # 
  return render(request, 'instructors/index.html', { 'instructors': instructors })

@login_required
def instructors_detail(request, instructor_id):
  instructor = Instructor.objects.get(id=instructor_id)
  # classes = Class.objects.exclude(id__in=instructor.classes.all().values_list('id'))
  return render(request, 'instructors/detail.html', {
    'instructor': instructor
    # 'instructor': instructor, 'classes': classes 
  })

# ________ Many-to-Many Associations __________

@login_required
def assoc_student(request, class_id, student_id):
  Class.objects.get(id=class_id).students.add(student_id)
  return redirect('classes_detail', class_id=class_id)

@login_required
def assoc_student_delete(request, class_id, student_id):
  Class.objects.get(id=class_id).students.remove(student_id)
  return redirect('classes_detail', class_id=class_id)

@login_required
def assoc_class(request, student_id, class_id):
  Student.objects.get(id=student_id).classes.add(class_id)
  return redirect('students_detail', student_id=student_id)

@login_required
def assoc_class_delete(request, student_id, class_id):
  Student.objects.get(id=student_id).classes.remove(class_id)
  return redirect('students_detail', student_id=student_id)


# Add Instructors Associatios Here
@login_required
def assoc_instructor_to_class(request, class_id, instructor_id):
  Class.objects.get(id=class_id).instructors.add(instructor_id)
  return redirect('classes_detail', class_id=class_id)

@login_required
def assoc_instructor_to_class_delete(request, class_id, instructor_id):
  Class.objects.get(id=class_id).instructors.remove(instructor_id)
  return redirect('classes_detail', class_id=class_id)

@login_required
def assoc_class_to_instructor(request, instructor_id, class_id):
  Instructor.objects.get(id=instructor_id).classes.add(class_id)
  return redirect('instructors_detail', instructor_id=instructor_id)

@login_required
def assoc_class_to_instructor_delete(request, instructor_id, class_id):
  Instructor.objects.get(id=instructor_id).classes.remove(class_id)
  return redirect('instructors_detail', instructor_id=instructor_id)

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

class ClassCreate(LoginRequiredMixin, CreateView):
  model = Class
  fields = ['title', 'studio', 'day_of_week', 'start_time', 'end_time', 'instructor']
  success_url = '/classes/'

class ClassUpdate(LoginRequiredMixin, UpdateView):
  model = Class
  fields = ['title', 'studio', 'day_of_week', 'start_time', 'end_time', 'instructor']
  success_url = '/classes/'

class ClassDelete(LoginRequiredMixin, DeleteView):
  model = Class
  success_url = '/classes/'

# ________ Class Declaration CRUD Functionality / Students __________

class StudentCreate(LoginRequiredMixin, CreateView):
  model = Student
  fields = ['name', 'email', 'phone', 'age', 'address', 'city', 'state', 'zip']
  success_url = '/students/'

class StudentUpdate(LoginRequiredMixin, UpdateView):
  model = Student
  fields = ['name', 'email', 'phone', 'age', 'address', 'city', 'state', 'zip']
  success_url = '/students/'

class StudentDelete(LoginRequiredMixin, DeleteView):
  model = Student
  success_url = '/students/'

# ________ Class Declaration CRUD Functionality / Instructor __________

class InstructorCreate(LoginRequiredMixin, CreateView):
  model = Instructor
  fields = ['name', 'email', 'phone']
  success_url = '/instructors/'

class InstructorUpdate(LoginRequiredMixin, UpdateView):
  model = Instructor
  fields = ['name', 'email', 'phone']
  success_url = '/instructors/'

class InstructorDelete(LoginRequiredMixin, DeleteView):
  model = Instructor
  success_url = '/instructors/'

