# Generated by Django 2.2.2 on 2020-08-30 21:46

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('firstname', models.CharField(default='', max_length=30, verbose_name='first name')),
                ('lastname', models.CharField(default='', max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('level', models.CharField(blank=True, choices=[('100', 'HUNDRED'), ('200', 'TWO HUNDRED'), ('300', 'THREE HUNDRED'), ('400', 'FOUR HUNDRED')], max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('programme', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('profile_pic', models.ImageField(blank=True, upload_to=accounts.models.upload_location1)),
                ('age', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('udated_on', models.DateTimeField(auto_now=True, verbose_name='updated on')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
