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

  # ________ Associated Links _________
  path('classes/<int:class_id>/assoc_student/<int:student_id>/', views.assoc_student, name='assoc_student'),
  path('classes/<int:class_id>/assoc_student/<int:student_id>/delete/', views.assoc_student_delete, name='assoc_student_delete'),

  # ________ Students _________
  path('students/', views.StudentList.as_view(), name='students_index'),
  path('students/<int:pk>', views.StudentDetail.as_view(), name='students_detail'),
  path('students/create', views.StudentCreate.as_view(), name='students_create'),
  path('students/<int:pk>/update', views.StudentUpdate.as_view(), name='students_update'),
  path('students/<int:pk>/delete', views.StudentDelete.as_view(), name='students_delete'),

  # ________ Sign-Up _________
  path('accounts/signup/', views.signup, name='signup'),
]