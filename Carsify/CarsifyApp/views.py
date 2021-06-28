from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def Index(request):
    News = False
    Con = False

    if request.method == 'POST':
        try:
            response = request.POST['nemail']
            Newsletter.objects.create(Email=response)
            News = True
            Con = False
            print(response)
            #send mail

        except:

            Name = request.POST['name']
            Phone = request.POST['number']
            City = request.POST['city']
            State = request.POST['state']
            Query = request.POST['query']
            Remark = request.POST['remark']
            Con = True
            News = False

            Contact.objects.create(Name = Name, Phone = Phone, City = City,  State = State,  Query = Query,  Remark= Remark)

            #send mail

    d = {"News": News, "Con": Con}

    return render(request, 'index.html', d)


def Login_Signup(request):
    error = False
    allready = False
    if request.method == 'POST':
        try:
            x = request.POST
            us = x['usr']
            pa = x['pas']
            user = authenticate(username=us, password=pa)

            if user:
                login(request, user)
                print("login")
                return redirect('CarsifyApp:Dashboard')
            else:
                error = True
        except:
            x = request.POST
            fullname = x['name']
            email = x['email']
            number = x['number']
            password = x['password']

            data = User.objects.filter(user=email)
            if(data):
                allready = True
            else:
                #create new user
                fname = fullname.split()
                User.objects.create_user(username=email, email=email, first_name=fname[0], last_name=fname[1], password=password)

    d = {"error": error, "allready":allready}
    return render(request, 'login.html', d)

def Logout(request):
    logout(request)
    return redirect('CarsifyApp:LoginSignup')


from django.contrib.auth.decorators import login_required

@login_required(login_url='CarsifyApp:LoginSignup')
def Dashboard(request):

    return render(request, 'dashboard.html')


@login_required(login_url='CarsifyApp:LoginSignup')
def Addcar(request):
    car_company = Car_Company.objects.all()

    dic = {'car_company':car_company}
    return render(request, 'addcar.html', dic)


@login_required(login_url='CarsifyApp:LoginSignup')
def Profile(request):
    useralldata = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        img = request.FILES["image"]
        useralldata.ProfileImg = img
        useralldata.save()
        return redirect('CarsifyApp:Profile')

    address = Address.objects.get(user=request.user)

    dic = {'useralldata':useralldata, 'useraddress': address}
    return render(request, 'profile.html', dic)


@login_required(login_url='CarsifyApp:LoginSignup')
def Editprofile(request):

    return render(request, 'editprofile.html')


@login_required(login_url='CarsifyApp:LoginSignup')
def Favourites(reqest):

    return render(reqest, 'favourites.html')


@login_required(login_url='CarsifyApp:LoginSignup')
def MYvehicle(request):

    return render(request, 'myvehicle.html')


@login_required(login_url='CarsifyApp:LoginSignup')
def Viewdetails(request):

    return render(request, 'viewdetails.html')