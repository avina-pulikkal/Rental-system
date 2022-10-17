from urllib import request
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import*
from .forms import*

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

# def weedviews(request):
#     cr=viewmodel.objects.all()
#     return render(request,"weedviews.html",{'cr':cr})


    return render(request,'plantviews.html')




# def portfoliodetails(request):
    # return render(request,'portfolio-details.html')



def Register(request):
    if request.method=="POST":
        id=request.POST.get('id')
        firstname=request.POST.get('firstname')
        middlename=request.POST.get('middlename')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        # img=request.POST.get('img')
        registermodel(firstname=firstname,middlename=middlename,lastname=lastname,address=address,phone=phone,gender=gender,email=email,psw=psw).save()
        return redirect('login')
    else:
        return render(request,'Register.html')



def login(request):
        return render(request,'login.html')
def log(request):
    if request.method=="POST":
        id=request.POST.get('id')

        email=request.POST.get('email')
        psw=request.POST.get('psw')
        # psw1=request.POST.get('psw1')


        cr=registermodel.objects.filter(email=email,psw=psw)
        if cr:
            user=registermodel.objects.get(email=email,psw=psw)
            id=user.id
            email=user.email
            psw=user.psw
            request.session['id']=id
            request.session['email']=email
            request.session['psw']=psw
            # request.session['psw1']=psw1
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'Register.html')

def home(request):
    #  if request.method=="POST" and request.FILES['myfile']:
    #     myfile=request.FILES['myfile']
    #     fs=FileSystemStorage()
    #     filename=fs.save(myfile.name,myfile)
    #     uploaded=fs.url(filename)
    #     print('uploaded',myfile.name)
    #     request.session['file']=myfile.name
    #     return render(request,'home.html',{
    #         'uploaded':uploaded
    #     })
     if request.method=="POST":
        # id=request.POST.get('id')
        name=request.POST.get('name')
        vehiclename=request.POST.get('vehiclename')
        price=request.POST.get('price')
        booking=request.POST.get('booking')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        # email=request.POST.get('email')
        # psw=request.POST.get('psw')
        # img=request.POST.get('img')
        bookingmodel(name=name,vehiclename=vehiclename,price=price,booking=booking,phone=phone,address=address).save()
     return render(request,'home.html')