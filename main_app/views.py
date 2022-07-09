from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import

import uuid
import boto3



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# ________ Many-to-Many Associations __________


# ________ Sign Up Function __________
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.post)
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


# ________ Class Declaration / __________


# ________ Class Declaration / __________

