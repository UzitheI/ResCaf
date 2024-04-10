# Generated by Django 5.0.3 on 2024-04-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=200)),
                ('country_of_origin', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='classicdish',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='italiandish',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='indiandish',
            name='cuisine',
        ),
        migrations.DeleteModel(
            name='ChineseDish',
        ),
        migrations.DeleteModel(
            name='ClassicDish',
        ),
        migrations.DeleteModel(
            name='ItalianDish',
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
        migrations.DeleteModel(
            name='IndianDish',
        ),
    ]