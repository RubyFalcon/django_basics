from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs ={
                "placeholder":"Your description",
                "class":"new class name two",
                "id":"my_id",
                "rows": 20,
                "cols":120,
            }))
    class Meta:
        model = Product 
        fields = ['title', 'description', 'price']

    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "CFE" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     if "news" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
    # def clean_email(self,*args,**kwargs):
    #     email = self.cleaned_data.get("email")
    #     if "@" not in email:
    #         raise forms.ValidationError("This is not a valid email")
            
class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs ={
                "placeholder":"Your description",
                "class":"new class name two",
                "id":"my_id",
                "rows": 20,
                "cols":120,
            }
            ))
    price = forms.DecimalField()
