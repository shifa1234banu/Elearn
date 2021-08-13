from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Tutor,Course
from django.contrib import messages
import random
from twilio.rest import Client
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CourseForm

# Create your views here.

@login_required(login_url='tsignin')
@never_cache
def dashboard(request):
    return render(request,"tutor/dashboard.html")


def tsignup(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            number = request.POST['number']
            password = request.POST['password']
            username = request.POST['username']


            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['number'] = number
            request.session['password'] = password
            request.session['username'] = username

        
            check_user = User.objects.filter(username=username).first()
            check_tutor = Tutor.objects.filter(number=number).first()
            
            if check_user or check_tutor:
                # context = {'message' : 'user already exist','class' : 'danger'}
                messages.info(request, 'username already exist')
                print('user')
                return render(request,'tutor/sign_up.html')
            # else:
            #     return render(request,"user/index.html") 

            account_sid = 'AC25dbb897684df02031b403539fede516'
            auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
            client = Client(account_sid, auth_token)

            verification = client.verify \
                                .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
                                .verifications \
                                .create(to='+91' +number, channel='sms')

            print(verification.status)


            return redirect('tsignupcheck')
    else:
        return render(request,"tutor/sign_up.html")    




def tsignupcheck(request):
    if request.method == 'POST':

        otp = request.POST['otp']

        first_name = request.session['first_name']
        last_name = request.session['last_name']
        email =  request.session['email']
        number = request.session['number']
        password = request.session['password']
        username = request.session['username']



        account_sid = 'AC25dbb897684df02031b403539fede516'
        auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
                                .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
                                .verification_checks \
                                .create(to='+91' +number, code=otp)

        print(verification_check.status)
        if verification_check.status == 'approved':
            user =User.objects.create_user(first_name =first_name,last_name=last_name,email=email,password=password,username=username,is_staff=True)
            user.save()

            
            
            
            tutor = Tutor()
            tutor.number=number
            tutor.user=user
            tutor.save()
            auth.login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
                
            print('working')
            # request.session['validnum'] = 'validnum'
            return redirect('index')



        del request.session['first_name']
        del request.session['last_name']
        del request.session['email']
        del request.session['number']
        del request.session['username'] 
        del request.session['password']   
 
    return render(request,"tutor/registerotp.html")

def tsignin(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'invalid credentials')
                return redirect('tsignin')
    else:
            
        return render(request,"tutor/sign_in.html") 


def totp(request):
    return render(request,"tutor/tutorotp.html")    


def totplogin(request):
    if request.method == 'POST':
        
        number = request.POST['number']
        is_user = Tutor.objects.filter(number=number).exists()
        if is_user :

            
            account_sid = 'AC25dbb897684df02031b403539fede516'
            auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
            client = Client(account_sid, auth_token)

            verification = client.verify \
                                .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
                                .verifications \
                                .create(to='+91' +number, channel='sms')

            print(verification.status)
            

           
            
            request.session['number'] = number
            return render(request,"user/enterotp.html")
        else:
            messages.info(request,"This phone number is not registered")
    else:    
        return redirect('tsignin')
    
def tsendotp(request):
    if request.method == 'POST':
        
        otp = request.POST['otp']
        number = request.session['number']
        
        account_sid = 'AC25dbb897684df02031b403539fede516'
        auth_token = '9e0a948e9f87c9459b0b54082fe36c31'
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
                                .services('VA02363701e6ab1e1cae6e1f2cf9b86670') \
                                .verification_checks \
                                .create(to='+91' +number, code=otp)

        print(verification_check.status)
        if verification_check.status == 'approved':
            tutor = Tutor.objects.get(number=number)
            user = profile.user
        
            auth.login(request,user,  backend='django.contrib.auth.backends.ModelBackend')
            print('loggedin')
            return redirect('index')
        
    return redirect('tsignin')                    
    







@login_required(login_url='tsignin')
@never_cache
def tlogout(request):
    auth.logout(request)
    print('logout')
    return redirect('tsignin')     



def tutorprofile(request):
    return render(request,'tutor/tutorprofile.html')
    

@login_required(login_url='adlogin')
def course(request):
    courses = Course.objects.all()
    
    return render(request,"tutor/course.html", {'courses' : courses})
    


@login_required(login_url='adlogin')
def addcourse(request):

    if request.method == 'POST':
        
        form = CourseForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('course')
        else:
            form = CourseForm()
            context ={'form':form}
            return render(request,"tutor/create_course.html",context)
                

    
    else:
        
        form = CourseForm()
        context ={'form':form}

        return render(request,"tutor/create_course.html",context)


@login_required(login_url='adlogin')
def editcourse(request, id):
    course = Course.objects.get(pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES,instance = course)
        
        if form.is_valid():
            form.save()
            print('working')
            return redirect('course')
           

        

    else:
        form = CourseForm(instance = course)
        return render(request,"tutor/editcourse.html" ,{'form' : form ,'course' : course})        