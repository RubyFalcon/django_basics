from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product

# Create your views here.
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # data valid
#             Product.objects.create(**my_form.cleaned_data)
#             print(my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request,"products/product_create.html", context)

# def product_create_view(request):
#     if request.method == "POST":
#         my_new_title = request.POST.get("title")
#         print(my_new_title)
#         # Products.objects.create(title=my_new_title)
#     context = {}
#     return render(request,"products/product_create.html", context)

def render_initial_data(request):
 
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,instance=obj)  
    if form.is_valid():
        form.save()
   
    context = {
        "form": form,
    }
    return render(request,"products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # re render on save
        form  = ProductForm()

    context = {
        "form": form,
    }

    return render(request,"products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
   
    context = {
        'object': obj
    }
    return render(request,"products/product_detail.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request,"products/product_detail.html",context)

def product_delete_view(request,id):
    obj = get_object_or_404(Product, id=id)
    # POST request for delete, by def its GET
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect("../../")
    context = {
        'object': obj
    }
    return render(request,"products/product_delete.html",context)

