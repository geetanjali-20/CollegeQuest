from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path("about",views.about, name='home'),
    path("services",views.services, name='home'),
    path("contact",views.contacts, name='home'),
    path("blogs",views.blog, name='home'),

]