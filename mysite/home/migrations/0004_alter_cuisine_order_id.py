# Generated by Django 5.0.3 on 2024-04-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_cuisine_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]