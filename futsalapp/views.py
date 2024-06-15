from django.shortcuts import render,redirect
from .models import *
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def booking(request):
    if request.method == 'POST':
        data = request.POST
        username = data['name']
        email = data['email']
        MblNumber = data['mobile']
        choose_futsal = data['futsal']
        calender = data['calender']
        time = data['time']

        obj = FutsalBooking.objects.create(
            username = username,
            email = email,
            mblnumber = MblNumber,
            futsal_choice = choose_futsal,
            date = calender,
            time = time
        )
        if obj:
            return redirect('detail')
    else:
              form = FutsalBooking()

    context = {
        'form': form,
    }

    return render(request,'booking.html',)





def detail(request):
    bookings = FutsalBooking.objects.all()
    context = {'bookings':bookings,}
    return render(request,'detail.html',context)

def delete(request,id):
     
     futsal = FutsalBooking.objects.get(id = id)
     if request.method == "POST":
          futsal.delete()
          return redirect('/detail')
     
     context = {"futsal":futsal}
     return render(request,"delete.html",context)
    


def update(request,id):
     
     futsal = FutsalBooking.objects.get(id = id)
     if request.method == "POST":
        futsal.username = request.Post['name']
        futsal.email = request.POSt['email']
        futsal.mblnumber = request.POST['mobile']
        futsal.futsal_choice = request.POST['futsal']
        futsal.date = request.POST['calender']
        futsal.time = request.POST['time']
        futsal.save()
        return redirect("/detail")\
        
     

     
     context = {'futsal':futsal}
     
     return render(request,"update.html",context)