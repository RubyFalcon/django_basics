from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args,**kwargs):
    return render(request,"home.html", {} )


def contact_view(request,*args,**kwargs):
    return render(request,"contact.html", {} )

def about_view(request,*args,**kwargs):
    my_context = {
        "titles": "this is about me",
        "my_number": 123,
        "is_real": True,
        "my_list": [1,2,3,"yes", True],
        "my_html": "<h1> Hello World </h1>"
    }
    return render(request,"about.html", my_context )

