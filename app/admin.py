from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group,User
from django.contrib import admin
from .models import Header,ContactUs

class HeaderAdmin(AdminSite):
    list_display=("title_body","icon")
    ordering=["id"]
admin.site.register(Header)
admin.site.register(ContactUs)
