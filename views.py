from django.shortcuts import render
from crudapp.models import Hospital

# Create your views here.


def read_data(request):
    Hospital_list=Hospital.objects.all()
    context={
        "Hospital_list":hospital_list
    }

    return render(request,"read.html",context)

def read_one_data(request,id):
    hspital=Hospital.objects.get(id=id)
    context={
        'hospital':hospital
    }
    return render(request,"readone.html",context)
    
