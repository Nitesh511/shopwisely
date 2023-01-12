from django.shortcuts import render, redirect
from accounts.auth import admin_only
from products.models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@admin_only
def dashboard(request):
    category = Category.objects.all()
    category_count = category.count()
    product= Products.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'category': category_count,
        'product': product_count,
        'order': order_count,
        'user': user_count,
        'admin': admin_count
    }

    return render(request,'admins/dashboard.html',context)


# @admin_only
# def order_status(request):
#     order = Order.

@admin_only
def update_status(request, order_id):
    order =Order.objects.get(id=order_id)
    order.status = "Delivered"
    order.save()
    messages.add_message(request, messages.SUCCESS, 'Order updated')
    return redirect('/admins/order')
