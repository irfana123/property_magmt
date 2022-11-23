import datetime
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from homeapp.models import Login, company, users, plan_details


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class companyRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])


    class Meta:
        model = company
        fields = ('name', 'contact_no', 'email', 'address',)


class UserRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])


    class Meta:
        model = users
        fields = ('name', 'contact_no', 'email', 'address',)


class uploadplanform(forms.ModelForm):
    class Meta:
        model=plan_details
        fields=('company','elevation','twod_plan','threed_plan','rooms','bathrooms','area',)