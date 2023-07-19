from django.shortcuts import render
from django.http import HttpResponse
from .models import departments,Doce
from .forms import BookingForm

# Create your views here.
def index(request):
   return render(request,'index.html')



def booking(request):
    if request.method == "POST":
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
    else:
      form =BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html', dict_form)

def doctors(request):
    dict_Docs={
        'Docs': Doce.objects.all()
    }
    return render(request,'doctors.html',dict_Docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept': departments.objects.all()
    }
    return render(request,'department.html',dict_dept)