from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import CategoryForm
from .models import Category
from learn_user.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def adsignincheck(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('adhome')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('adsignin')
    else:
        return redirect('adsignin')



def adsignin(request):
    return render(request,'admin/login.html')



def adhome(request):
    return render(request,'admin/ad_dashboard.html')    


def user(request):
    
    queryset = Profile.objects.all()
    context = {'profiles' : queryset}
    return render(request,"admin/usermanagement.html",context)


    
@login_required(login_url='adlogin')
def blockuser(request, id):
    user=User.objects.get(pk=id)
    user.is_active = False
    user.save()

    return redirect('user')

@login_required(login_url='adlogin')
def unblockuser(request, id):
    user=User.objects.get(pk=id)
    user.is_active = True
    user.save()

    return redirect('user')  


@login_required(login_url='adsignin')
def category(request):
    
    categories = Category.objects.all()
    return render(request,"admin/category.html", {'categories' : categories})

    
@login_required(login_url='adsignin')
def addcategory(request):
   
    if request.method == 'POST':
        
        form = CategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            print('working')
            return redirect('category')

    
    else:
        form = CategoryForm()
        context ={'form':form}

        return render(request,"admin/addcategory.html",context)

@login_required(login_url='adsignin')
def editcategory(request,id):
    category = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance = category)
        
        if form.is_valid():
            form.save()
            print('working')
            return redirect('category')

        

    else:
        form = CategoryForm(instance = category)
        return render(request,"admin/edit category.html" ,{'form' : form ,'category' : category})



@login_required(login_url='adsignin')
def categorycheck(request, id):
    

        category = Category.objects.get(pk=id)
        category.delete()
        return redirect('category')         