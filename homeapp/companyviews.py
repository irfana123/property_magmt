from django.shortcuts import render


def company_home(request):
    return render(request,'companytemp/chome.html')