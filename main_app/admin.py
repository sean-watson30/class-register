from django.contrib import admin
from .models import Class, Student, Instructor

# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Instructor)