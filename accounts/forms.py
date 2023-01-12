from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile
class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user', 'username','email']
