from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from homeapp.models import company, users, userComplaint, plan_details


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

def viewplan(request):
    plan = plan_details.objects.all()

    return render(request,'admintemp/viewplan.html',{'plan':plan})


def viewcomplaint(request):
    data= userComplaint.objects.all()
    return render(request,'admintemp/viewcomplaint.html',{'data':data})


def reply_complaint(request, id):
    complaint = userComplaint.objects.get(id=id)
    # complaint2 = StdntComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('viewcomplaint')
    return render(request, 'admintemp/replycomplaints.html', {'complaint': complaint})



def viewpayment(request):
    return render(request,'admintemp/viewpayment.html')
