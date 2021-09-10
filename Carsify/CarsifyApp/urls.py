from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
app_name = "CarsifyApp"

urlpatterns = [
    path('', Index, name='Index'),
    # path('login/', Login_Signup, name='LoginSignup'),
    path('logout/', Logout, name='Logout'),
    # path('signup/', Signup, name='Signup'),
    #dashboard
    path('dashboard/', Dashboard, name='Dashboard'),

    path('addcar/', Addcar, name='Addcar'),
    path('addcarsuccess/', Addcarsuccess, name='Addcarsuccess'),

    #addcardadvaceux
    path('cars-json', json_Car_add, name='cars-json'),
    path('addcar/models-json/<str:car>', json_Car_model, name='models-json'),

    #profile
    path('profile/', Profile, name='Profile'),
    path('editprofile/', Editprofile, name='Editprofile'),

    #filterdata
    path('filter-data', filter_data, name='filter_data'),

    path('myvehicle/', MYvehicle, name='MYvehicle'),

    #vehicle status
    path('editvehicle/<int:cid>', Edit_Vehicle_Details, name='Edit_Vehicle_Details'),
    path('editvehicleimage/<int:cid>', Edit_Vehicle_Images, name='Edit_Vehicle_Images'),
    path('deletevehicleimage/', Delete_Vehicle_Image, name='Delete_Vehicle_Image'),
    path('disable/<int:cid>', Disable_My_Vehicle, name='Disable_My_Vehicle'),
    path('enable/<int:cid>', Enable_My_Vehicle, name='Enable_My_Vehicle'),
    
    #path('deletemycar/<int:cid>', Delete_My_Car, name='Delete_My_Car'),


    path('viewdetails/<int:cid>', Viewdetails, name='Viewdetails'),
    path('mailimages/<int:cid>', MailImages, name='MailImages'),
    path('downloadimages/<int:cid>', DownloadImages, name='DownloadImages'),
    path('favourites/', Favourites, name='Favourites'),
    path('delete_from_favourite/<int:cid>', Delete_From_Favourite, name='Delete_From_Favourite'),
    path('add_favourite_car/<int:cid>',Add_to_Favourite, name='Add_to_Favourite'),

    url(r'^login/', Login_Signup, name="LoginSignup" ),
    url(r'^signup/', Signup, name="Signup" )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)