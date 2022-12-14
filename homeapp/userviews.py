from django.contrib import messages
from django.shortcuts import render, redirect

from homeapp.forms import request_plan_form, userComplaintForm
from homeapp.models import users, company, plan_details, plan_request, userComplaint


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

def requestplans(request):
    u=request.user
    form = request_plan_form()
    if request.method == 'POST':
        form = request_plan_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('user_home')
    return render(request,'usertemp/requestplan.html',{'form':form})

def viewrequest(request):
    u=request.user
    data=plan_request.objects.filter(user=u)
    return render(request,'usertemp/viewrequests.html',{'data':data})

def viewreqreply(request,id):
    data=plan_request.objects.get(id=id)


    return render(request,'usertemp/viewreqreply.html',{'data':data})


def addcomplaint(request):
    form = userComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = userComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('user_home')
    else:
        form = userComplaintForm()
    return render(request,'usertemp/addcomplaint.html',{'form':form})


def complaintview(request):
    n = userComplaint.objects.filter(user=request.user)
    return render(request, 'usertemp/viewselfcomplaint.html', {'n': n})


def purchaseplans(request):
    return render(request,'usertemp/purchasepge.html')
