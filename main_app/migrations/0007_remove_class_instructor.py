# Generated by Django 4.0.6 on 2022-07-11 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_class_instructor_class_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='instructor',
        ),
    ]
