# Generated by Django 4.0.6 on 2022-07-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_class_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='instructor',
        ),
        migrations.AddField(
            model_name='instructor',
            name='classes',
            field=models.ManyToManyField(related_name='classes', to='main_app.class'),
        ),
    ]
