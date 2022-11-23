from django.shortcuts import render, redirect

from homeapp.forms import uploadplanform
from homeapp.models import company, plan_details


def company_home(request):
    return render(request,'companytemp/chome.html')

def profile_view(request):
    u = request.user
    profile = company.objects.filter(user=u)
    return render(request,'companytemp/profile.html',{'profile':profile})


def upload_plans(request):
    form = uploadplanform()
    if request.method == 'POST':
        form = uploadplanform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_plans')
    return render(request, 'companytemp/upload_plans.html', {'form': form})




def view_plans(request):
    u=request.user
    plans=plan_details.objects.filter(company=u)
    return render(request,'companytemp/view_plans.html',{'plans':plans})

def update_plans(request,id):
    user = plan_details.objects.get(id=id)
    form = uploadplanform(instance=user)
    if request.method == "POST":
        form = uploadplanform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('view_plans')
    return render(request,'companytemp/updateplans.html',{'form':form})

def view_planrequests(request):
    return render(request,'companytemp/requests.html')

def chatwithuser(request):
    return render(request,'companytemp/chatwithuser.html')

def reviews(request):
    return render(request,'companytemp/reviews.html')