# Generated by Django 2.0.5 on 2018-06-07 09:57

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Data', '0005_auto_20180607_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='MA106_Date',
            fields=[
                ('Date', models.DateField(default='2018-06-07', primary_key=True, serialize=False)),
                ('Status', models.CharField(default='NA', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='ma106',
            name='June_4_2018',
        ),
        migrations.AddField(
            model_name='ma106',
            name='Dates',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), default=[], max_length=176, size=16),
        ),
    ]