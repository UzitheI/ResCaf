# Generated by Django 5.0.3 on 2024-04-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_usersuggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersuggestions',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]