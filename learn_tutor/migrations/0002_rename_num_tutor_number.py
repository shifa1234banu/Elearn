# Generated by Django 3.2 on 2021-07-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn_tutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='num',
            new_name='number',
        ),
    ]
