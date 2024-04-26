from django.urls import *
from . import views

urlpatterns = [
    path('navbar', views.navbar, name='navbar'),
    path('', views.signup, name='signup'),
    path('contactus', views.contactus, name='contactus'),
    path('feedback', views.feedback, name='feedback'),
    path('submit_feedback', views.submit_feedback, name='submit_feedback'),
    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('loader', views.loader, name='loader'),
    path('services', views.services, name='services'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('checkforgot', views.checkforgot, name='checkforgot'),
    path('rashichart', views.rashichart, name='rashichart'),
    path('rasi', views.rasi, name='rasi'),
    path('input', views.input, name='input'),
    path('horoscope', views.horoscope, name='horoscope'),
    path('zodiacsign', views.zodiacsign, name='zodiacsign'),
    path('profile', views.profile, name="profile"),
    path('userdetails', views.userdetails, name='userdetails'),
    path('checksignup', views.checksignup, name="checksignup"),
    path('checksignin', views.checksignin, name='checksignin'),
    path('checkotp', views.checkotp, name='checkotp'),
    path('changepass', views.changepass, name='changepass'),
    path('checkcontact', views.checkcontact, name='checkcontact'),
    path('checkuserdetails', views.checkuserdetails, name="checkuserdetails"),
]
