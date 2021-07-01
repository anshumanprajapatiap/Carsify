from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
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

'''
def Login_Signup(request):
    error = False
    allready = False
    if request.method == 'POST':
        x = request.POST
        try:
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
'''

def Login_Signup(request):
    error = False
    not_exist = False
    if request.method == 'POST':
        x = request.POST

        us = x['usr']
        pa = x['pas']
        user = authenticate(username=us, password=pa)
        data = User.objects.filter(username=us)
        if user:
            login(request, user)
            print("login")
            return redirect('CarsifyApp:Dashboard')
        else:
            if data:
                error = True
            else:
                not_exist=True

    d = {"error": error, "not_exist": not_exist}
    return render(request, 'login.html', d)

def Signup(request):
    allready = False
    if request.method == 'POST':
        x = request.POST
        fullname = x['name']
        email = x['email']
        number = x['number']
        password = x['password']

        data = User.objects.filter(username=email)
        if (data):
            allready = True
        else:
            # create new user
            fname = fullname.split()
            user = User.objects.create_user(username=email, email=email, first_name=fname[0], last_name=fname[1],
                                     password=password)
            UserProfile.objects.create(user=user)
            type = Address_Type.objects.all()
            for i in type:
                Address.objects.create(user=user, Address_Typee=i)

        return redirect('CarsifyApp:LoginSignup')

def Logout(request):
    logout(request)
    return redirect('CarsifyApp:LoginSignup')


from django.contrib.auth.decorators import login_required

@login_required(login_url='CarsifyApp:LoginSignup')
def Dashboard(request):
    car_data = Individual_Car_Details.objects.all()
    car_company_data = Car_Company.objects.all()
    fuels = Car_Fuel.objects.all()

    if request.GET:
        q = request.GET['q']
        car_data = Individual_Car_Details.objects.filter(Company__icotanins=q).order_by('-id')

    dic = {'car_data': car_data, 'car_company_data': car_company_data, 'fuels':fuels}

    return render(request, 'dashboard.html', dic)



@login_required(login_url='CarsifyApp:LoginSignup')
#filter data
def filter_data(request):
    car_company = request.GET.getlist('company_of_car[]')
    print(car_company)
    fuel = request.GET.getlist('fuel[]')

    car_data = Individual_Car_Details.objects.all().order_by('-id')

    #filters
    if len(car_company) > 0:
        car_data = car_data.filter(Company__id__in=car_company).distinct()

    if len(fuel) > 0:
        car_data = car_data.filter(Fuel_Type__id__in=fuel).distinct()

    t = render_to_string('allcarlist.html', {'car_data': car_data})
    return JsonResponse({'data':t})


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

    address = Address.objects.filter(user=request.user)

    dic = {'useralldata':useralldata, 'useraddress': address}
    return render(request, 'profile.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Editprofile(request):

    return render(request, 'editprofile.html')

@login_required(login_url='CarsifyApp:LoginSignup')
def Favourites(request):
    data = UserFavouriteCars.objects.filter(user=request.user)

    dic = {'f_Car':data}
    return render(request, 'favourites.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def MYvehicle(request):
    data = Individual_Car_Details.objects.filter(user=request.user)
    dic = {'m_Car': data}
    return render(request, 'myvehicle.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Edit_Vehicle_Details(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    dic={'data':data}
    return render(request, 'index.html', dic)

#edit individual and update function
@login_required(login_url='CarsifyApp:LoginSignup')
def Edit_Update(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    dic = {'data': data}
    return render(request, 'index.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Disable_My_Vehicle(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    data.Individual_Car_Details.objects.update(Car_Status=True)

@login_required(login_url='CarsifyApp:LoginSignup')
def Delete_My_Car(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    data.delete()

    return redirect('CarsifyApp:MYvehicle')

@login_required(login_url='CarsifyApp:LoginSignup')
def Viewdetails(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    dic ={'data':data}
    return render(request, 'viewdetails.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Delete_From_Favourite(request,cid):
    data = UserFavouriteCars.objects.get(id=cid)
    data.delete()
    return redirect('CarsifyApp:Favourites')

@login_required(login_url='CarsifyApp:LoginSignup')
def Add_to_Favourite(request, cid):
    UserFavouriteCars.objects.create(user=request.user, carid=cid)
    return redirect('CarsifyApp:Dashboard')