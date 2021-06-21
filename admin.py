from django.contrib import admin
from crudapp.models import Hospital

# Register your models here.


class HospitalAdmin(admin.ModelAdmin):
    list_display=['name','doctor','patient','city','contact']




admin.site.register(Hospital,HospitalAdmin)