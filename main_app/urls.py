from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('about/', views.about, name='about'),
  path('classes/', views.classes_index, name='classes_index'),

  path('accounts/signup/', views.signup, name='signup'),
]