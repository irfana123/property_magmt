from django.urls import path

from homeapp import views, adminviews, companyviews, userviews

urlpatterns = [
path('',views.home,name='home'),
path('loginview',views.loginview,name='loginview'),
path('admin_home',adminviews.admin_home,name='admin_home'),
path('company_register',views.company_register,name='company_register'),
path('user_register',views.user_register,name='user_register'),
path('company_home',companyviews.company_home,name='company_home'),
path('user_home',userviews.user_home,name='user_home'),
    ]