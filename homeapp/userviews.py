from django.shortcuts import render

from homeapp.models import users


def user_home(request):
    return render(request,'usertemp/uhome.html')


def userprofile(request):
    u=request.user
    profile=users.objects.filter(user=u)
    return render(request,'usertemp/profile.html',{'profile':profile})