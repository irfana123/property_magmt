from django.shortcuts import render

from homeapp.models import company


def company_home(request):
    return render(request,'companytemp/chome.html')

def profile_view(request):
    u = request.user
    profile = company.objects.filter(user=u)
    return render(request,'companytemp/profile.html',{'profile':profile})


def upload_plans(request):
    return render(request,'companytemp/upload_plans.html')


def view_plans(request):
    return render(request,'companytemp/view_plans.html')

def view_planrequests(request):
    return render(request,'companytemp/requests.html')

def chatwithuser(request):
    return render(request,'companytemp/chatwithuser.html')

def reviews(request):
    return render(request,'companytemp/reviews.html')