import django_filters
from .models import Products
from django_filters import CharFilter

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = "__all__"
        exclude=['product_price','product_image','category','created_date']