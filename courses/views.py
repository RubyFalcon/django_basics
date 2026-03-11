from django.shortcuts import render
from django.views import View


# BASE VIEW class = VIEW
# Create your views here.
class CourseDetailView(View):
    template_name = "about.html"

    def get(self,request, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})
    
def my_fbv(req,*arg,**kwargs):
    return render(req, "about.html", {})