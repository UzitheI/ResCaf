# Generated by Django 5.0.3 on 2024-04-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
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
    ]
