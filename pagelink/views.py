
from .models import Destination

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    # print("here1 {0}".format(request))
    if request.method=='POST':
        # email=request.POST['email']
        password=request.POST['password']
        username=request.POST['name']
        # print("here3 {0} {1}".format(email,password))
        user=auth.authenticate(username=username,password=password)
        # print("here4 {0}".format(user))
        if user is not None:
            auth.login(request, user)
            # print("here5")
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        # first_name=request.POST['first_name']
        username=request.POST['name']
        password1=request.POST['password']
        # password2=request.POST['password2']
        email=request.POST['email']

        user=User.objects.create_user(username=username,password=password1,email=email)
        user.save()
        print('user created')
        return redirect('login')


    else:
        return render(request,'register.html')


def dash(request):
    dests=Destination.objects.all()
    return render(request,'dash.html',{'dests': dests})


def post(request):
    if request.method=='POST':
        name=request.POST['name']
        img=request.FILES['img']
        desc=request.POST['desc']
        price=request.POST['price']
        phone=request.POST['phone']
        user=Destination.objects.create(name=name,img=img,desc=desc,price=price)
        user.save()
        return redirect('joblist')
    else:
        return render(request,'post.html')


def searchresult(request):
    query=request.POST['name']
    alpost=Destination.objects.filter(name__icontains=query)


    return render(request,'searchresult.html',{'alpost':alpost,'query':query})

def search(request):
    # user=request.GET['username']
    # user=auth.authenticate(username=username,password=password,email=email)
    # if request.user.is_authenticated:

        # return render(request,'profile.html',{'user':user})
        return render(request,'search.html')
    # else:
        # return redirect('login')
def logout(request):
    auth.logout(request)
    messages.info(request,'you are logout')
    return redirect('/')

def about(request):
    return render(request,'about.html')


def blog(request):
    return render(request,'blog.html')

def joblist(request):
    dests=Destination.objects.all()
    return render(request,'joblist.html',{'dests': dests})

def profile(request):
    return render(request,'profile.html')

def my_func(request):
    return HttpResponse(request, "this is on click")
    # document.getElementById('remove-heli-' + dest).style.visibility = 'hidden'

