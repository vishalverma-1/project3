#-----CREATE REGISTRATION PAGE--------
from django.shortcuts import render,redirect
from django . http import HttpResponse
from . models import company

def create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        obj=company.objects.create(name=name,email=email,mobile=mobile)
        obj.save()
        return redirect('home')
    else:
        return render(request,'create.html')
    
#--------HOME PAGE----------

def home(request):
    obj=company.objects.all()
    return render(request,'home.html',{'obj':obj})

#---------DELETE PAGE----------

def delete(request,id):
    obj=company.objects.get(id=id)
    obj.delete()
    return redirect('home')
#---------EDIT PAGE-----------
 
def edit(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        data=company.objects.filter(id=id).update(name=name,email=email,mobile=mobile)
        return redirect('home')
    else:
        data1=company.objects.filter(id=id)
        return render(request,'edit.html',{'data1':data1})
  



