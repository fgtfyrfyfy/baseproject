from django.contrib import admin
from .models import employee,student
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','salary')

admin.site.register(employee)
admin.site.register(student)