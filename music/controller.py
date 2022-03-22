from unicodedata import name
from django.urls import path
from music.forms import Register
from music.views import Home,Dts,signup,signin,AddAlbum,upalbum,Delalbum,Addsong
from . import views
app_name='music'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path("<int:pk>",Dts.as_view(),name='detail'),
    path("signup",signup.as_view(),name='Register'),
    path("signin",signin.as_view(),name='login'),
    path("album/uploadalbum",AddAlbum.as_view(),name='addalbum'),
    path("album/update/<int:pk>/",upalbum.as_view(),name='upalbum'),
    path("album/delete/<int:pk>/",Delalbum.as_view(),name='delalbum'),
    path("album/song/add/<int:pk>/",Addsong.as_view(),name='addsong'),
    path("album/song/update/<int:pk>/",views.upsong.as_view(),name='upsong'),
    path("album/song/delete/<int:pk>/",views.delsong.as_view(),name='delsong'),
    path("signout",views.signout,name='logout'),
    path('user/addprofile',views.AddProfile.as_view(),name='addprofile'),
    path('user/profile',views.show_profile,name='profile'),

]