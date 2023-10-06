from django.urls import path
from . import views

urlpatterns = [
    path('addeducation/',views.addeducation,name='addeducation'),
    path('addexperience/',views.addexperience,name='addexperience'),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('dashbord/',views.dashbord,name='dashbord'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('profiles/',views.profiles,name='profiles'),
    path('register/',views.register,name='register'),
]

