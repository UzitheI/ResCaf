# Generated by Django 4.2.13 on 2024-06-06 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_cartitem_accept_button_cartitem_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='accept_button',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='reject_button',
        ),
    ]
