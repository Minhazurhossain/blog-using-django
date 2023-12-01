from django import forms
from django.contrib.auth.forms import UserChangeForm,UserChangeForm
from django.contrib.auth.models import User
from login.models import UserProfile

class SignUpForm(UserChangeForm):
    email = forms.EmailField(label="Email Address",required=True)
    class  Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)