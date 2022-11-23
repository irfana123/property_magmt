from django.shortcuts import render

from homeapp.models import users, company, plan_details


def user_home(request):
    return render(request,'usertemp/uhome.html')


def userprofile(request):
    u=request.user
    profile=users.objects.filter(user=u)
    return render(request,'usertemp/profile.html',{'profile':profile})

def viewcompany(request):
    data=company.objects.all()
    return render(request,'usertemp/viewcompany.html',{'data':data})

def viewplans(request):
    plan=plan_details.objects.all()
    return render(request,'usertemp/viewplans.html',{'plan':plan})
