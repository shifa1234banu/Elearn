from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Profile,CartItem,Purchase
from django.contrib import messages
import random
from twilio.rest import Client
from django.views.decorators.cache import never_cache
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from learn_tutor.models import Course,Category
from django.http import JsonResponse
import razorpay
from django.db.models import Q,Count
import stripe
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

# This is your real test secret API key.

# stripe.api_key = 'sk_test_51JLNKBSB1uVeqLYarlEA27gh7jlEDVmS6Oye24EQsXnde2YurQzjL5kT7Ok32DVxJ9Msw6MlbOFwL1DmWJ9qYhbH00j3jkSbry'


def index(request):
    user=request.user
    
    category = Category.objects.all()
    course = Course.objects.all()
    context = {'courses' : course,
            'categories' : category,
           
            
            
                }
               
    
        
    return render(request,"user/index.html",context)

    


@never_cache
def signin(request):
     
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    cart_item = CartItem.objects.get(cart=cart)
                    cart_item.user= user
                    cart_item.save()
                except:
                    pass 
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'invalid credentials')
                return redirect('signin')
        else:
            return render(request,"user/sign_in.html")



def registerotp(request):
    return render(request,"user/otpregister.html")               

def signup(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            num = request.POST['num']
            password = request.POST['password']
            username = request.POST['username']


            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['num'] = num
            request.session['password'] = password
            request.session['username'] = username

        
            check_user = User.objects.filter(username=username).first()
            check_profile = Profile.objects.filter(num=num).first()
            
            if check_user or check_profile:
                # context = {'message' : 'user already exist','class' : 'danger'}
                messages.info(request, 'username already exist')
                print('user')
                return render(request,'user/sign_up.html')
            # else:
            #     return render(request,"user/index.html") 

            # account_sid = 'AC25dbb897684df02031b403539fede516'
            # auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
            # client = Client(account_sid, auth_token)

            # verification = client.verify \
            #                     .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
            #                     .verifications \
            #                     .create(to='+91' +num, channel='sms')

            # print(verification.status)


            return redirect('signupcheck')
    else:
        return render(request,"user/sign_up.html")    




def signupcheck(request):
    if request.method == 'POST':

        otp = request.POST['otp']

        first_name = request.session['first_name']
        last_name = request.session['last_name']
        email =  request.session['email']
        num = request.session['num']
        password = request.session['password']
        username = request.session['username']



        # account_sid = 'AC25dbb897684df02031b403539fede516'
        # auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
        # client = Client(account_sid, auth_token)

        # verification_check = client.verify \
        #                         .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
        #                         .verification_checks \
        #                         .create(to='+91' +num, code=otp)

        print(verification_check.status)
        if verification_check.status == 'approved':
            user =User.objects.create_user(first_name =first_name,last_name=last_name,email=email,password=password,username=username)
            user.save()

            
            
            
            profile = Profile()
            profile.num=num
            profile.user=user
            profile.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                
            print('working')
            # request.session['validnum'] = 'validnum'
            return redirect('index')



        del request.session['first_name']
        del request.session['last_name']
        del request.session['email']
        del request.session['num']
        del request.session['username'] 
        del request.session['password']   
 
    return render(request,"user/enterregister.html")


@login_required(login_url='signin')
@never_cache
def logout(request):
    auth.logout(request)
    return redirect('/')    

def otphtml(request):
    return render(request,"user/otplogin.html")    


def otplogin(request):
    if request.method == 'POST':
        
        num = request.POST['num']
        is_user = Profile.objects.filter(num=num).exists()
        if is_user :

            
            # account_sid = 'AC25dbb897684df02031b403539fede516'
            # auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
            # client = Client(account_sid, auth_token)

            # verification = client.verify \
            #                     .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
            #                     .verifications \
            #                     .create(to='+91' +num, channel='sms')

            # print(verification.status)
            

           
            
            request.session['num'] = num
            return render(request,"user/enterotp.html")
        else:
            messages.info(request,"This phone number is not registered")
    else:    
        return redirect('signin')
    
def sendotp(request):
    if request.method == 'POST':
        
        otp = request.POST['otp']
        num = request.session['num']
        
        # account_sid = 'AC25dbb897684df02031b403539fede516'
        # auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
        # client = Client(account_sid, auth_token)

        # verification_check = client.verify \
        #                         .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
        #                         .verification_checks \
        #                         .create(to='+91' +num, code=otp)

        # print(verification_check.status)
        if verification_check.status == 'approved':
            profile = Profile.objects.get(num=num)
            user = profile.user
        
            auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            print('loggedin')
            return redirect('index')
        
    return redirect('signin')                    
    
 
def userprofile(request):
    user =request.user
    profile = Profile.objects.get(user=user)
    imageform = ImageForm(instance=profile)
    context={'imageform':imageform,
                'profile':profile,  
                }

    if request.method == 'POST':
        print('work')
        
        imageform = ImageForm(request.POST , request.FILES , instance=profile)

        if imageform.is_valid():
            print('worked')
            imageform.save()

        
    return render(request,"user/userprofile.html",context)




def edit(request, id):
        
        user = User.objects.get(pk=id)
        profile = Profile.objects.get(pk=id)
       
        context={'user':user,
                  'profile':profile,  
                }
        return render(request,'user/editprofile.html',context)
                
 
    
def editcheck(request, id):

    
        if request.method == 'POST':
        
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            num = request.POST['num']
        
            User.objects.filter(pk=id).update(first_name=first_name,last_name=last_name,email=email,username=username)
            Profile.objects.filter(pk=id).update(num=num)
            
            return redirect('userprofile')
        else:
            return redirect('edit')      
                     

def coursedetails(request,id):
     
    course = Course.objects.get(id=id)
    context={'courses' : course}
    return render(request,"user/coursedetail.html",context)         


login_required(login_url='signin')
def add_cart(request):
    id = int(request.GET['id'])
   
    user = request.user
    course = Course.objects.get(id=id)

    try:
        cart_item = CartItem.objects.get(course=course, user=user)
        cart_item.save()
        print('saved')
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            course = course,
           
            user=user
        )
        cart_item.save()
        print('item saved')
    
    return JsonResponse({'data':True})    


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

def cart(request):
    user=request.user
    cart_items=None
    total=0

    try:
        cart_items = CartItem.objects.filter(user=user, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.course.price)
 
    except ObjectDoesNotExist:
        pass

    context ={
        'total' : total,
        'cart_items' : cart_items,
        }
    return render(request,"user/cart.html",context)



def remove_cart_item(request,id):
    CartItem.objects.filter(id=id).delete()
    return redirect('cart')   


@never_cache
def checkout(request,total=0):
    cart_items = None
    try:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.course.price)
    
    except ObjectDoesNotExist:
        pass
    
    
    context ={
        'amount' : total,
        'cart_items' : cart_items,
        }
    

    return render(request,"user/checkout.html",context)
    


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            courses = Course.objects.filter(Q(course_name__icontains=keyword) | Q(short_des__icontains=keyword))
            course_count = courses.count()
        else:
            return render(request,"user/index.html")    
    context = {
        'courses' : courses,
        'course_count' : course_count,
    }
    return render(request,"user/search_result.html",context)

     


    
def categorycourse(request,id):
    category = Category.objects.get(id=id)
    cat = Course.objects.filter(category=category)
    context={'cat' : cat}
    return render(request,"user/category.html",context)




@never_cache
def stripe(request,total=0):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        if not cart_items:
            return redirect('index')
        for cart_item in cart_items:
            total += (cart_item.course.price)
            amount = total
            print(amount,'////////')

            request.session['payment_method'] = 'pay'
            pay_method = request.session['payment_method']
            purchase = Purchase.objects.create(user=request.user,item=cart_item.course,price=cart_item.course.price,pay_method=pay_method)
            purchase.save()
            print(cart_item,'-------------',)
            cart_item.delete()

           
    
        return render(request,"user/success.html") 



@never_cache
def invoice(request):
    user=request.user
    purchase = Purchase.objects.filter(user=user)

    context = {
        'user': user,
        'purchase' : purchase,
        }
    
    return render(request,"user/invoice.html",context)




def allcourse(request):
    course = Course.objects.all()

    context = {'courses':course}
    return render(request,"user/allcourse.html",context)        