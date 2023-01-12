from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Loginform,createUserForm,ProfileForm
from .auth import unauthenticated_user,admin_only,user_only
from django.contrib.auth.decorators import login_required
from products.models import Order, Cart
from .models import Profile
# Create your views here.


def homepage(request):
    # cart_items = Cart.objects.filter(user=request.user)
    # cart_count = cart_items.count()
    # context = {
    #     'cart_no': cart_count
    # }

    return render(request,'accounts/homepage.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')


@unauthenticated_user
def login_user(request):
    if request.method =="POST":
        form = Loginform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins/dashboard')
                elif not user.is_staff:
                    login(request,user)
                    return redirect('/products/homepage')

            else:
                messages.add_message(request,messages.ERROR,'invalid User credintials')
                return render(request,'accounts/login.html',{'form_login':form})
    context ={
        'form_login':Loginform,
        'activate_login':'active'
    }
    return render(request,'accounts/login.html',context)


@unauthenticated_user
def register_user(request):
    if request.method =="POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username)
            messages.add_message(request,messages.SUCCESS,'User Registred SUcesfully')
            return redirect('/login')
        else:
            messages.add_message(request,messages.ERROR,'Unable To Register User')
            return render(request,'accounts/register.html',{'form_register':form})
    context = {
        'form_register': createUserForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)

@login_required
@admin_only
def get_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users':users
    }
    return render(request, 'accounts/users.html', context)

@login_required
@admin_only
def get_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins':admins
    }
    return render(request, 'accounts/admins.html', context)


@login_required
@admin_only
def get_orders(request):
    items = Order.objects.all()
    status = Order.STATUS
    context = {
        'items': items,
        'status': status,

    }
    return render(request,'accounts/order_status.html',context)

@login_required
@user_only
def profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/profile')
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, 'accounts/profile.html', context)

@login_required
@admin_only
def promote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/admins')

@login_required
@admin_only
def demote_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin demoted to user')
    return redirect('/admins/users')

@login_required
@admin_only
def deactivate_admin(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Disabled')
    return redirect('/admins/users')

@login_required
@admin_only
def deactivate_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Disabled')
    return redirect('/admins/users')

@login_required
@admin_only
def activate_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Activated')
    return redirect('/admins/users')
@login_required
@admin_only
def activate_admin(request,user_id):
    user = User.objects.get(id=user_id)
    user.is_active=True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Activated')
    return redirect('/admins/users')