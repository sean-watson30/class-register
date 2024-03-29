# Generated by Django 4.0.6 on 2022-07-12 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_rename_instructor_class_instructors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='instructors',
        ),
        migrations.AddField(
            model_name='class',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.instructor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
