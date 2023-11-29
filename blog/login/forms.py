from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserChangeForm):
    email = forms.EmailField(label="Email Address",required=True)
    class  Meta:
        model = User
        fields = ('username','email','password','password')
