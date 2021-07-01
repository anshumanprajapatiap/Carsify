from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "CarsifyApp"

urlpatterns = [
    path('', Index, name='Index'),
    path('login/', Login_Signup, name='LoginSignup'),
    path('logout/', Logout, name='Logout'),
    path('signup/', Signup, name='Signup'),
    #dashboard
    path('dashboard/', Dashboard, name='Dashboard'),
    path('addcar/', Addcar, name='Addcar'),
    path('profile/', Profile, name='Profile'),
    path('editprofile/', Editprofile, name='Editprofile'),

    #filterdata

    path('filter-data', filter_data, name='filter_data'),

    path('myvehicle/', MYvehicle, name='MYvehicle'),
    path('viewdetails/<int:cid>', Viewdetails, name='Viewdetails'),
    path('favourites/', Favourites, name='Favourites'),
    path('delete_from_favourite/ <int:cid>', Delete_From_Favourite, name='Delete_From_Favourite'),
    path('add_favourite_car/ <int:cid>',Add_to_Favourite, name='Add_to_Favourite'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)