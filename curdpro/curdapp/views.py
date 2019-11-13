from django.shortcuts import render
from django.http.response import HttpResponse
from .models import ProductData
from .forms import InsertDataForm,UpdatedataForm,DeleteDataForm

def index(request):
    return render(request,'index.html')

def create_view(request):
    if request.method == "POST":
        iform = InsertDataForm(request.POST)
        if iform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_class = request.POST.get('product_class')
            product_color = request.POST.get('product_color')
            product_weight = request.POST.get('product_weight')
            product_cost = request.POST.get('product_cost')

            data = ProductData(
                product_id=product_id,
                product_name=product_name,
                product_class=product_class,
                product_color=product_color,
                product_weight=product_weight,
                product_cost=product_cost
            )
            data.save()
            iform = InsertDataForm()
            return render(request,'insertdata.html',{'iform':iform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        iform = InsertDataForm()
        return render(request,'insertdata.html',{'iform':iform})


def retrieve_view(request):
    products = ProductData.objects.all()
    return render(request,'retrievedata.html',{"products":products})

def update_view(request):
    if request.method == "POST":
        uform = UpdatedataForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')

            pid = ProductData.objects.filter(product_id=product_id)

            if pid:
                pid.update(product_cost = product_cost)
                uform = UpdatedataForm()
                return render(request,'updatedata.html',{'uform':uform})
            else:
                return HttpResponse("Product ID is not available")
        else:
            return HttpResponse("User Invalid Data")
    else:
        uform = UpdatedataForm()
        return render(request,'updatedata.html',{'uform':uform})

def delete_view(request):
    if request.method == "POST":
        dform = DeleteDataForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            pid = ProductData.objects.filter(product_id=product_id)
            if pid:
                pid.delete()
                dform = DeleteDataForm()
                return render(request,'deletedata.html',{'dform':dform})
            else:
                return HttpResponse("Product Is Not Available")
        else:
            return HttpResponse("User Invalid Data")
    else:
        dform = DeleteDataForm()
        return render(request,'deletedata.html',{'dform':dform})