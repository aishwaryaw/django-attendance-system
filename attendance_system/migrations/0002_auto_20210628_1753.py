# Generated by Django 3.0.6 on 2021-06-28 12:23

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Employee name must be valid', regex='^[a-zA-Z-,]+(\\s{0,1}[a-zA-Z-, ])*$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.DateField(default=datetime.date(2021, 6, 28)),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
