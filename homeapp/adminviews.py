from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from homeapp.models import company



def admin_home(request):
    return render(request,'admintemp/index.html')


@login_required(login_url='loginview')
def view_company(request):
    n = company.objects.all()

    return render(request, 'admintemp/nurse.html', {'n':n})
