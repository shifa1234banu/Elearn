# Generated by Django 3.2 on 2021-08-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='media/categories'),
        ),
    ]
