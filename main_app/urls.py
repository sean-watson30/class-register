from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('about/', views.about, name='about'),
  # ________ Classes _________
  path('classes/', views.classes_index, name='classes_index'),
  path('classes/<int:class_id>', views.classes_detail, name='classes_detail'),
  path('classes/create/', views.ClassCreate.as_view(), name='classes_create'),
  path('classes/<int:pk>/update/', views.ClassUpdate.as_view(), name='classes_update'),
  path('classes/<int:pk>/delete/', views.ClassDelete.as_view(), name='classes_delete'),

  # ________ Students _________


  # ________ Sign-Up _________
  path('accounts/signup/', views.signup, name='signup'),
]