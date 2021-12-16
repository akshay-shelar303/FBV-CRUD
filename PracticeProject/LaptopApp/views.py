from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm

def addLaptop(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
    template_name = "LaptopApp/laptop.html"
    context = {'form':form}
    return render(request, template_name, context)

def showLaptop(request):
    laptop_list = Laptop.objects.all()
    template_name = "LaptopApp/showlaptop.html"
    context = {'laptop_list': laptop_list}
    return render(request, template_name, context)

def updateView(request,i):
    laptop = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
    template_name = "LaptopApp/laptop.html"
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request,i):
    laptop = Laptop.objects.get(id=i)
    if request.method == 'POST':
        laptop.delete()
        return redirect("show_laptop")
    template_name = "LaptopApp/confirmdelete.html"
    context = {'laptop': laptop}
    return render(request, template_name, context)