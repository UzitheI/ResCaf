# Generated by Django 5.0.3 on 2024-04-19 01:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('position', models.CharField(max_length=244)),
                ('description', models.CharField(max_length=244)),
                ('image', models.CharField(max_length=244)),
                ('facebook', models.CharField(max_length=244)),
                ('twitter', models.CharField(max_length=244)),
                ('pinterest', models.CharField(max_length=244)),
                ('linkedin', models.CharField(max_length=244)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('table_price', models.FloatField()),
                ('table_description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=224)),
                ('description', models.CharField(max_length=224)),
                ('header_image', models.CharField(max_length=224)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
                ('writer_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('stars', models.FloatField()),
                ('description', models.TextField()),
                ('dish', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.dish')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookATable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=233)),
                ('customer_email', models.EmailField(max_length=254)),
                ('numberOfPeople', models.IntegerField()),
                ('dateOfBooking', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.table')),
            ],
        ),
    ]
