# Generated by Django 2.0.5 on 2018-06-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Data', '0011_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=20),
        ),
    ]
