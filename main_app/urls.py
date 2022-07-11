from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # ________ Instructors _________
  path('instructors/', views.instructors_index, name='instructors_index'),
  path('instructors/<int:instructor_id>', views.instructors_detail, name='instructors_detail'),
  path('instructors/create/', views.InstructorCreate.as_view(), name='instructors_create'),
  path('instructors/<int:pk>/update/', views.InstructorUpdate.as_view(), name='instructors_update'),
  path('instructors/<int:pk>/delete/', views.InstructorDelete.as_view(), name='instructors_delete'),
  
  # ________ Classes _________

  path('classes/', views.classes_index, name='classes_index'),
  path('classes/<int:class_id>', views.classes_detail, name='classes_detail'),
  path('classes/create/', views.ClassCreate.as_view(), name='classes_create'),
  path('classes/<int:pk>/update/', views.ClassUpdate.as_view(), name='classes_update'),
  path('classes/<int:pk>/delete/', views.ClassDelete.as_view(), name='classes_delete'),

  # ________ Associated Links _________

  path('classes/<int:class_id>/assoc_student/<int:student_id>/', views.assoc_student, name='assoc_student'),
  path('classes/<int:class_id>/assoc_student/<int:student_id>/delete/', views.assoc_student_delete, name='assoc_student_delete'),

# add instructor to class?
  path('classes/<int:class_id>/assoc_instructor/<int:instructor_id>/', views.assoc_instructor, name='assoc_instructor'),
  path('classes/<int:class_id>/assoc_instructor/<int:instructor_id>/delete/', views.assoc_instructor_delete, name='assoc_instructor_delete'),
# 

  path('students/<int:student_id>/assoc_class/<int:class_id>/', views.assoc_class, name='assoc_class'),
  path('students/<int:student_id>/assoc_class/<int:class_id>/delete/', views.assoc_class_delete, name='assoc_class_delete'),


  # ________ Students _________

  # path('students/', views.StudentList.as_view(), name='students_index'),
  # path('students/<int:pk>', views.StudentDetail.as_view(), name='students_detail'),
  path('students/', views.students_index, name='students_index'),
  path('students/<int:student_id>', views.students_detail, name='students_detail'),
  path('students/create', views.StudentCreate.as_view(), name='students_create'),
  path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='students_update'),
  path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='students_delete'),

  # ________ Sign-Up _________

  path('accounts/signup/', views.signup, name='signup'),
]