from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from homeapp.forms import LoginRegister, companyRegister, UserRegister


def home(request):
    return render(request,'index.html')


def loginview(request):
    print("hi")
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                print("hiiii")
                return redirect('admin_home')
            elif user.is_company:
                return redirect('company_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request,'loginpage.html')

def company_register(request):
    user_form = LoginRegister()
    company_form = companyRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        company_form = companyRegister(request.POST)
        if user_form.is_valid() and company_form.is_valid():
            user = user_form.save(commit=False)
            user.is_company = True
            user.save()
            company = company_form.save(commit=False)
            company.user = user
            company.save()
            messages.info(request, 'company Registered Successfully')
            return redirect('loginview')
    return render(request, 'register.html', {'user_form': user_form, 'company_form': company_form})


def user_register(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, 'User Registered Successfully')
            return redirect('login_view')
    return render(request, 'register.html', {'login_form': login_form, 'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect('login_view')
