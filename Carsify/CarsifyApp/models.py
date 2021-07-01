from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class India_States(models.Model):
    State_Name = models.TextField(null=True)
    def __str__(self):
        return self.State_Name

class Contact(models.Model):
    Name = models.TextField(null=True)
    Phone = models.IntegerField(null=True)
    City = models.TextField(null=True)
    State = models.TextField(null=True)
    Query = models.TextField(null=True)
    Remark = models.TextField(null=True)

    def __int__(self):
        return self.Phone

class Newsletter(models.Model):
    Email = models.EmailField(null=True)

    def __str__(self):
        return self.Email

class Address_Type(models.Model):
    Type = models.TextField(null=True)

    def __str__(self):
        return self.Type

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Address_Typee = models.ForeignKey(Address_Type, on_delete=models.CASCADE, null=True)
    street_address = models.CharField(max_length=100, null=True)
    apartment_address = models.CharField(max_length=100, null=True)
    City = models.TextField(null=True)
    State = models.TextField(null=True)
    country = models.TextField(null=True)
    zip = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username + ' -- ' + self.Address_Typee.Type

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ProfileImg = models.FileField(null=True)
    ContactNo = models.IntegerField(null=True)
    Email = models.EmailField(null=True)
    Address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)
    #Documents
    AddharNumber = models.IntegerField(null=True)
    PanNumber = models.TextField(null=True)
    VoterID = models.TextField(null=True)

    def __str__(self):
        return self.user.username

#all about cars from here

class Car_Company(models.Model):
    Car_Company_Name = models.TextField(null=True)
    def __str__(self):
        return self.Car_Company_Name

class Car_Fuel(models.Model):
    Car_Fuel_Type = models.TextField(null=True)
    def __str__(self):
        return self.Car_Fuel_Type

class Transmission_Type(models.Model):
    Tranmission = models.TextField(null=True)
    def __str__(self):
        return self.Tranmission


class Car_Model(models.Model):
    Company_Name = models.ForeignKey(Car_Company,on_delete=models.CASCADE,null=True)
    Car_Model_Name = models.TextField(null=True)

    def __str__(self):
        return self.Company_Name.Car_Company_Name +' -- '+ self.Car_Model_Name


class Individual_Car_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Company = models.ForeignKey(Car_Company,on_delete=models.CASCADE,null=True)
    Model = models.ForeignKey(Car_Model,on_delete=models.CASCADE,null=True)
    Registration_State = models.ForeignKey(India_States, on_delete=models.CASCADE, null=True)
    Fuel_Type = models.ForeignKey(Car_Fuel, on_delete=models.CASCADE, null=True)
    Transmission = models.ForeignKey(Transmission_Type, on_delete=models.CASCADE, null=True)

    Car_Status = models.BooleanField(default=False)

    Date_of_Manufacturing = models.DateField(null=True)
    Card_Registration_Number = models.TextField(null=True)
    Car_Varient = models.TextField(null=True)
    KM = models.IntegerField(null=True)
    Color = models.TextField(null=True)
    Images = models.ImageField(null=True)
    Price = models.IntegerField(null=True)
    Insurance = models.TextField(null=True)
    Insurance_Type = models.TextField(null=True)

    def __str__(self):
        return self.user.username+' -- '+ self.Card_Registration_Number


class Individual_Car_Images(models.Model):
    carid = models.ForeignKey(Individual_Car_Details,on_delete=models.CASCADE,null=True)
    Image1 = models.ImageField(null=True)
    Image2 = models.ImageField(null=True)
    Image3 = models.ImageField(null=True)
    Image4 = models.ImageField(null=True)
    Image5 = models.ImageField(null=True)
    Image6 = models.ImageField(null=True)
    Image7 = models.ImageField(null=True)
    Image8 = models.ImageField(null=True)
    Image9 = models.ImageField(null=True)
    Image10 = models.ImageField(null=True)

    def __str__(self):
        return self.carid

#user Favourites cars
class UserFavouriteCars(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    carid = models.ForeignKey(Individual_Car_Details,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username+' -- '+ self.carid.Card_Registration_Number
