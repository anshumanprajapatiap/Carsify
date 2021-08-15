from django.db.models.base import Model
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.db.models import Min,Max,Q
import datetime
# import CarsifyApp.image_processing
# views.py file

from django.contrib.auth.hashers import check_password
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
    return render(request,'login.html')


def Logout(request):
    logout(request)
    return redirect('CarsifyApp:LoginSignup')


from django.contrib.auth.decorators import login_required

@login_required(login_url='CarsifyApp:LoginSignup')
def Dashboard(request):
    
    car_data = Individual_Car_Details.objects.filter(Car_Status=False)
    car_company_data = Car_Company.objects.all()
    fuels = Car_Fuel.objects.all()
    transmission_type = Transmission_Type.objects.all()
    owners = Number_of_Owners.objects.all()
    Body_Types = Car_Body_Type.objects.all()
    minmaxPrice = Individual_Car_Details.objects.aggregate(Min('Price'), Max('Price'))
    minmaxYear = Individual_Car_Details.objects.aggregate(Min('Date_of_Manufacturing'), Max('Date_of_Manufacturing'))
    minmaxKm = Individual_Car_Details.objects.aggregate(Min('KM'), Max('KM'))
    states = India_States.objects.all()
    Companies = Car_Company.objects.values()
    fav_ids = []
    
    for i in UserFavouriteCars.objects.filter(user=request.user).values():
        fav_ids.append(i.get('carid_id'))

    if request.GET: 
        if 'q' in request.GET:
            q = request.GET['q']
            ids=[]
            companyData = Companies.filter(Car_Company_Name__icontains =q)
            for data in companyData:
                ids.append(data.get('id'))  
            car_data = Individual_Car_Details.objects.filter(Company_id__in=ids).order_by('-id')
            if(q.strip()==""):
                print("A")
                car_data = Individual_Car_Details.objects.filter(Car_Status=False)
            

    dic = {'car_data': car_data, 'car_company_data': car_company_data, \
           'fuels':fuels,'transmission_type':transmission_type,'owners':owners, \
           'car_body_types':Body_Types, 'Minmaxprice':minmaxPrice, 'minmaxYear': minmaxYear, 'minmaxKm': minmaxKm, 'states':states,'fav_id':fav_ids}

    return render(request, 'dashboard.html', dic)



@login_required(login_url='CarsifyApp:LoginSignup')
#filter data
def filter_data(request):
    car_company = request.GET.getlist('company_of_car[]')
    fuel = request.GET.getlist('fuel[]')
    transmission_type = request.GET.getlist('transmission[]')
    owners = request.GET.getlist('owner[]')
    car_body_type = request.GET.getlist('car_body_type[]')
    state = request.GET.getlist('state[]')
    minPrice = request.GET['minPrice']
    maxPrice = request.GET['maxPrice']
    minYear = request.GET['minYear']
    maxYear = request.GET['maxYear']
    minKm = request.GET['minKm']
    maxKm = request.GET['maxKm']
    car_data = Individual_Car_Details.objects.filter(Car_Status=False)
    #sort
    sort = request.GET['orderby']    

    if sort=="price+":
        car_data = car_data.order_by('-Price')
        # car_data = request.GET.get('sort','-Price')
        
    elif sort == "price-":
        car_data = car_data.order_by('Price')

    elif sort == "year+":
        car_data = car_data.order_by('-Date_of_Manufacturing')
    elif sort == "year-":
        car_data = car_data.order_by('Date_of_Manufacturing')

    #price  
    car_data = car_data.filter(Price__gte=minPrice)
    car_data = car_data.filter(Price__lte=maxPrice)

    #Km
    car_data = car_data.filter(KM__gte= minKm)
    car_data = car_data.filter(KM__lte= maxKm)

    #Year
    minYeardate = datetime.date(int(minYear), 1, 1)
    maxYeardate = datetime.date(int(maxYear), 12, 31)
    print(minYeardate, maxYeardate)
    car_data = car_data.filter(Date_of_Manufacturing__gte= minYeardate)
    car_data = car_data.filter(Date_of_Manufacturing__lte= maxYeardate)



    #filters
    if len(car_company) > 0:
        car_data = car_data.filter(Company__id__in=car_company).distinct()

    if len(fuel) > 0:
        car_data = car_data.filter(Fuel_Type__id__in=fuel).distinct()

    if len(transmission_type) > 0:
        car_data = car_data.filter(Transmission__id__in=transmission_type).distinct()

    if len(owners) > 0:
        car_data = car_data.filter(Owners__id__in=owners).distinct()

    if len(car_body_type) > 0:
        car_data = car_data.filter(Body_Type__id__in=car_body_type).distinct()

    t = render_to_string('allcarlist.html', {'car_data': car_data})
    return JsonResponse({'data':t})


def Addcarsuccess(request):

    return render(request, 'addcarsuccess.html')

@login_required(login_url='CarsifyApp:LoginSignup')
def Addcar(request):
    car_company = Car_Company.objects.all()
    car_model = Car_Model.objects.all()
    registeredstate = India_States.objects.all()
    numberofowners = Number_of_Owners.objects.all()
    vehicletype = Car_Body_Type.objects.all()
    tansmission = Transmission_Type.objects.all()
    fueltype = Car_Fuel.objects.all()


    if request.method == "POST":
        x = request.POST
        companyname = x['companyname']
        companyobj = Car_Company.objects.get(id=companyname)
        modelidd = x['modelname']
        modelname = Car_Model.objects.get(id=modelidd)
        VehicleNumber = x['VehicleNumber']
        Varient = x['Varient']
        RegisteredStateidd = x['RegisteredState']
        RegisteredState = India_States.objects.get(id=RegisteredStateidd)
        Registeredcity = x['Registeredcity']
        NumberofOwnersidd = x['NumberofOwners']
        NumberofOwners = Number_of_Owners.objects.get(id=NumberofOwnersidd)
        Manufacturing = x['Manufacturing']
        DManufacturing = datetime.date(int(Manufacturing), 1, 1)
        VehicalTypeidd = x['VehicalType']
        VehicalType = Car_Body_Type.objects.get(id=VehicalTypeidd)
        Transmissionidd = x['Transmission']
        Transmission = Transmission_Type.objects.get(id=Transmissionidd)
        Km = x['Km']
        color = x['color']
        FuelTypeidd = x['FuelType']
        FuelType = Car_Fuel.objects.get(id=FuelTypeidd)
        Price = x['Price']
        Insurance = x['Insurance']
        InsuranceType = x['InsuranceType']
        Comment = x['Comment']

        #handeling multiple images
        Images = request.FILES.getlist('Images')
        showimage = Images[0]

        #create a vehicle object here
        cid = Individual_Car_Details.objects.create(user=request.user, Company=companyobj, Model=modelname,\
            Registration_State=RegisteredState, Fuel_Type =FuelType, Transmission=Transmission, Owners=NumberofOwners,\
            Body_Type=VehicalType, Date_of_Manufacturing = DManufacturing, Card_Registration_Number=VehicleNumber,\
            Car_Varient=Varient, KM=Km, Color=color, Price=Price, Insurance=Insurance, Insurance_Type=InsuranceType, \
            City=Registeredcity, Discription=Comment, Showimage=showimage)

        #creating image objects
        for image in Images:
            photo = Individual_Car_Images.objects.create(carid=cid, Image=image)

        #return success page
        return redirect('CarsifyApp:Addcarsuccess')
        
    
    
    dic = {'car_company':car_company, 'car_model':car_model, 'registeredstate':registeredstate,\
            'numberofowners': numberofowners, 'vehicletype': vehicletype, 'tansmission':tansmission,\
           'fueltype':fueltype}

    return render(request, 'addcar.html', dic)

def json_Car_add(request):
    car_company = list(Car_Company.objects.values())

    return JsonResponse({'data':car_company})

def json_Car_model(request, *args, **kwarg):
    selecedted_car = kwarg.get('car')
    obj_models = list(Car_Model.objects.filter(Company_Name=selecedted_car).values())

    return JsonResponse({'data':obj_models})

@login_required(login_url='CarsifyApp:LoginSignup')
def Profile(request):
    
    try:
        useralldata = UserProfile.objects.get(user=request.user)
    except:
        useralldata = None


    if useralldata:
        if request.method == "POST":
            img = request.FILES["image"]
            useralldata.ProfileImg = img
            useralldata.save()
            return redirect('CarsifyApp:Profile')
    
    else:
        user = request.user
        UserProfile.objects.create(user=user)
        type = Address_Type.objects.all()
        for i in type:
            Address.objects.create(user=user, Address_Typee=i)
    Aadhar = str(useralldata.AddharNumber)[0:4]+" "+str(useralldata.AddharNumber)[4:8]+" "+str(useralldata.AddharNumber)[8:12]
    address = Address.objects.filter(user=request.user)[0]

    dic = {'useralldata':useralldata, 'useraddress': address,'Aadhar':Aadhar}
    return render(request, 'profile.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Editprofile(request):

    try:
        useralldata = UserProfile.objects.get(user=request.user)
    except:
        useralldata = None

    if useralldata:
        print("hello")
    else:
        user = request.user
        UserProfile.objects.create(user=user)
        type = Address_Type.objects.all()
        for i in type:
            Address.objects.create(user=user, Address_Typee=i)
    
        user = request.user
        UserProfile.objects.create(user=user)
        type = Address_Type.objects.all()
        for i in type:
            Address.objects.create(user=user, Address_Typee=i)

    has_password = False
    if request.user.has_usable_password:
        has_password:True

    types = Address_Type.objects.all()
    address = Address.objects.filter(user=request.user)[0]
    Aadhar = "XXXX XXXX XXXX"
    if useralldata.AddharNumber is not None:
        Aadhar = str(useralldata.AddharNumber)[0:4]+" "+str(useralldata.AddharNumber)[4:8]+" "+str(useralldata.AddharNumber)[8:12]

    if request.method == 'POST':
        if 'profilePicBtn' in request.POST:
            img = request.FILES["image"]
            useralldata.ProfileImg = img
            useralldata.save()
        if 'profileBtn' in request.POST:
            x = request.POST
            useralldata.AddharNumber = int(x.get('aadhar').replace(" ",""))
            useralldata.PanNumber = x.get('panNumber')
            useralldata.VoterID = x.get('voterId')
            useralldata.ContactNo = x.get('contactNo')
            useralldata.Email = x.get('EmailAddress')
            NewAddress = x.get("Address").split(",")
            x = NewAddress[0].split(":-")[0].capitalize()
            print(NewAddress)
            if( x=="Home"):
                address.Address_Typee= types[0]
            elif(x=="Work"):
                address.Address_Typee = types[1]
            else:
                address.Address_Typee= types[0]
            address.apartment_address = NewAddress[0].split(":-")[1]
            address.street_address = NewAddress[1]
            address.City = NewAddress[2]
            address.State = NewAddress[3]
            address.country = NewAddress[4]
            address.zip = NewAddress[5]
            address.save()
            useralldata.save()
            return redirect('CarsifyApp:Profile')

        elif 'changePass' in request.POST:
            x=request.POST
            password = request.user.password
            currPass = x.get('currPass')
            newPass = x.get('newPass')
            rePass = x.get('rePass')
            print(currPass)
            print(newPass)
            print(rePass)
            if not(has_password):
                if(newPass==currPass):
                    request.user.set_password(newPass)
                    request.user.save()
                    return redirect('CarsifyApp:Profile')
                else:
                    return render(request, 'editprofile.html',{'useralldata':useralldata, 'useraddress': address, 'alert_flag':True,'msg':"New Password and Re-entered Password does not match!",'Password':not(has_password),"Aadhar":Aadhar})

            matchcheck = check_password(currPass,password)
            if matchcheck:
                if not(newPass == currPass):
                    if newPass==rePass:
                        request.user.set_password(newPass)
                        request.user.save()
                        return redirect('CarsifyApp:Profile')
                    else:
                        return render(request, 'editprofile.html',{'useralldata':useralldata, 'useraddress': address, 'alert_flag':True,'msg':"New Password and Re-entered Password does not match!",'Password':not(has_password),"Aadhar":Aadhar})
                elif newPass==currPass:
                    print("Same")
                    return render(request, 'editprofile.html',{'useralldata':useralldata, 'useraddress': address, 'alert_flag':True,'msg':"New Password cannot be Old Password!",'Password':not(has_password),"Aadhar":Aadhar})
            else:      
                return render(request, 'editprofile.html',{'useralldata':useralldata, 'useraddress': address, 'alert_flag':True,'msg':"Current Password Does not match",'Password':not(has_password),"Aadhar":Aadhar})

    dic = {'useralldata':useralldata, 'useraddress': address,'alert_flag':False,'Password':not(has_password),"Aadhar":Aadhar}

    return render(request, 'editprofile.html',dic)

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
    Companies = Car_Company.objects.all()
    car_model = []
    states = India_States.objects.all()
    owners = Number_of_Owners.objects.all() 
    fav_ids = []
    fav = False
    for i in UserFavouriteCars.objects.filter(user=request.user).values():
        fav_ids.append(i.get('carid_id'))
    if cid in fav_ids:
        fav=True
    
    if request.POST:
        x = request.POST
        data.Company = Car_Company.objects.get(Car_Company_Name=x.get('companyname'))
        # data.Model = x.get('model')
        data.Registration_State = India_States.objects.get(id=x.get('registrationState'))
        data.City = x.get('City')
        data.Owners = Number_of_Owners.objects.get(id=x.get('owner'))
        data.Discription = x.get('description').lstrip(" ")
        data.Price = x.get('Price')
        data.Card_Registration_Number = x.get('RegistrationNumber')
        data.save()
        #  Fuel_Type =FuelType, Transmission=Transmission,
        #     Body_Type=VehicalType, Date_of_Manufacturing = DManufacturing,
        #     Car_Varient=Varient, KM=Km, Color=color, Insurance=Insurance, Insurance_Type=InsuranceType, \
        # Showimage=showimage


    dic={'data':data,'fav':fav,'states':states,'companies':Companies,'car_model':car_model,'owners':owners}
    return render(request, 'editmyvehicle.html', dic)

#edit individual and update function
@login_required(login_url='CarsifyApp:LoginSignup')
def Edit_Update(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    dic = {'data': data}
    return redirect('CarsifyApp:MYvehicle')

@login_required(login_url='CarsifyApp:LoginSignup')
def Disable_My_Vehicle(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    # Individual_Car_Details.objects.update(id = cid, Car_Status=True)
    data.Car_Status = True
    data.save()
    return redirect('CarsifyApp:MYvehicle')

@login_required(login_url='CarsifyApp:LoginSignup')
def Enable_My_Vehicle(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    # Individual_Car_Details.objects.update(id = cid, Car_Status=True)
    data.Car_Status = False
    data.save()
    return redirect('CarsifyApp:MYvehicle')


@login_required(login_url='CarsifyApp:LoginSignup')
def Delete_My_Car(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    data.delete()
    return redirect('CarsifyApp:MYvehicle')

@login_required(login_url='CarsifyApp:LoginSignup')
def Viewdetails(request, cid):
    data = Individual_Car_Details.objects.get(id=cid)
    images = Individual_Car_Images.objects.filter(carid=data)
    cdata = UserFavouriteCars.objects.filter(carid=data)
    userdata =  UserProfile.objects.get(user = data.user)
    a_list = len(images)
    noimages = list(range(1, a_list+1))
        
    dic ={'data':data, 'images':images, 'noimages':noimages, 'cdata':cdata, 'udata':userdata}
    return render(request, 'viewdetails.html', dic)

@login_required(login_url='CarsifyApp:LoginSignup')
def Delete_From_Favourite(request,cid):

    data = UserFavouriteCars.objects.get(user=request.user,carid=cid)
    data.delete()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='CarsifyApp:LoginSignup')
def Add_to_Favourite(request, cid):
    all = False
    data = Individual_Car_Details.objects.get(id=cid)
    try:
        there = UserFavouriteCars.objects.get(user=request.user,carid=data)
    except:
        there=None

    if there:
        all=True
    else:
        UserFavouriteCars.objects.create(user=request.user, carid=data)

    return redirect(request.META.get('HTTP_REFERER'))