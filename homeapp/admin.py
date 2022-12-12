from django.contrib import admin

# Register your models here.
from homeapp.models import *

admin.site.register(Login)
admin.site.register(company)
admin.site.register(users)
admin.site.register(plan_details)
admin.site.register(plan_request)