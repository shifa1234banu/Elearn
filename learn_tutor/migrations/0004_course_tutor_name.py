# Generated by Django 3.2 on 2021-08-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_tutor', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor_name',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]