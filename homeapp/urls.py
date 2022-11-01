from django.urls import path

from homeapp import views, adminviews

urlpatterns = [
path('',views.home,name='home'),
path('loginview',views.loginview,name='loginview'),
path('admin_home',adminviews.admin_home,name='admin_home'),
path('company_register',views.company_register,name='company_register'),
path('user_register',views.user_register,name='user_register'),
    ]