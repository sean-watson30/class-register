# Generated by Django 4.0.6 on 2022-07-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_class_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='studio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
