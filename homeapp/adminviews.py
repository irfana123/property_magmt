from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from homeapp.models import company, users


def admin_home(request):
    return render(request,'admintemp/ahome.html')



def view_company(request):
    print("hello")
    n = company.objects.all()
    print(n)

    return render(request,'admintemp/viewcompany.html', {'n':n})

def view_users(request):
    print("hello")
    n = users.objects.all()
    print(n)

    return render(request,'admintemp/viewusers.html', {'n':n})
