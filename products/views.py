from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # Only render title, desc and price for now
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    # }
    context = {
        'object': obj
    }
    return render(request,"products/product_detail.html", context)