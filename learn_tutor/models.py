from django.db import models
from django.contrib.auth.models import User
from learn_admin.models import Category

# Create your models here.


class Tutor(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    number = models.CharField(max_length=15,unique=True)
    
    userimage = models.ImageField(null=True,blank=True,upload_to='photos/productimages',default='user/images/user.png')
    
   


    def __str__(self):
        return str(self.number)



class Course(models.Model):
    video1= models.FileField(upload_to='videos', null=True, verbose_name="")
    video2= models.FileField(upload_to='videos', null=True, verbose_name="")
    video3= models.FileField(upload_to='videos', null=True, verbose_name="")
    video4= models.FileField(upload_to='videos', null=True, verbose_name="")
    video5= models.FileField(upload_to='videos', null=True, verbose_name="")
    video6= models.FileField(upload_to='videos', null=True, verbose_name="")
    video7= models.FileField(upload_to='videos', null=True, verbose_name="")
    video8= models.FileField(upload_to='videos', null=True, verbose_name="")
    preview_video = models.FileField(upload_to='videos', null=True, verbose_name="")
    course_name = models.CharField(max_length=50)
    course_des = models.CharField(max_length=1000)
    short_des = models.CharField(max_length=5000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    course_image =  models.ImageField(upload_to='courseimages')
    tutor_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.course_name

