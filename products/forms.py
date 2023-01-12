from django import forms
from django.forms import ModelForm
from .models import Category,Products,Order


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address','payment_method']