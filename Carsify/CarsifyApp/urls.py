from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "CarsifyApp"

urlpatterns = [
    path('', Index, name='Index'),
    path('login/', Login_Signup, name='LoginSignup'),
    path('logout/', Logout, name='Logout'),

    #dashboard
    path('dashboard/', Dashboard, name='Dashboard'),
    path('addcar/', Addcar, name='Addcar'),
    path('profile/', Profile, name='Profile'),
    path('editprofile/', Editprofile, name='Editprofile'),
    path('myvehicle/', MYvehicle, name='MYvehicle'),
    path('viewdetails/', Viewdetails, name='Viewdetails'),
    path('favourites/', Favourites, name='Favourites'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)