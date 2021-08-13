# Generated by Django 3.2 on 2021-08-03 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn_admin', '0003_alter_category_cat_image'),
        ('learn_tutor', '0002_rename_num_tutor_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video1', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video2', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video3', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video4', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video5', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video6', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video7', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('video8', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('preview_video', models.FileField(null=True, upload_to='videos', verbose_name='')),
                ('course_name', models.CharField(max_length=50)),
                ('course_des', models.CharField(max_length=1000)),
                ('short_des', models.CharField(max_length=5000)),
                ('price', models.IntegerField()),
                ('course_image', models.ImageField(upload_to='courseimages')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_admin.category')),
            ],
        ),
    ]