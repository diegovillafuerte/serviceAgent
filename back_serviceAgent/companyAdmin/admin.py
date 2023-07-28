
from django.contrib import admin
from companyAdmin.models import CompanyUser

class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')  # Add 'id' and 'user' to the list display

admin.site.register(CompanyUser, CompanyUserAdmin)