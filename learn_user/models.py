from django.db import models
from django.contrib.auth.models import User
from learn_tutor.models import Course
import uuid

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    num = models.CharField(max_length=15,unique=True)
    
    userimage = models.ImageField(null=True,blank=True,upload_to='photos/productimages',default='user/images/user.png')
    
   


    def __str__(self):
        return str(self.num)



class Cart(models.Model):
    
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    


class CartItem(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return self.course.price * self.quantity        



class Purchase(models.Model):
    PAYMENT_STATUS = {                                                                                  
            ('Success','Success'),
            ('Failed','Failed'),
            ('Pending','Pending'),
        }

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Course,on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    price = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=True)
    purchase_time = models.TimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='Success')
    pay_method = models.CharField(max_length=100,default=100)
    


    def __str__(self):
        return self.item         