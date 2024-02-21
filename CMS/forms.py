from django import forms
from .models import Order,Customer,Product,Tags
from django.forms import Select, DateInput,TextInput,EmailInput

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {'customer':'Customer','product':'Product','date_created':'Date_created','status':'Status',}
        widgets = {
            'customer': Select(attrs={'class': 'form-control'}),
            'product': Select(attrs={'class': 'form-control'}),
            'date_created': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {'name':'Name','phone':'Phone','email':'Email','date_created':'Date_created'}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter your name','class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Enter your phone number','class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email','class': 'form-control'}),
            'date_created': DateInput(attrs={'type': 'date','class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","category","tags"]  # You can also specify the fields you want to include instead of '__all__'
        labels = {'name':'Name Of Product','price':'Price','category':'Category','Tags':'tags'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'checkbox-list'}),
        }


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'
        labels = {'name':'Name'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }

