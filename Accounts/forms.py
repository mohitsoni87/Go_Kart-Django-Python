from django import forms
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password = password)
        if username and password:
            if not user:               # to check if the password is correct
                raise forms.ValidationError("Invalid Credentials")
            if not user.is_active:
                raise forms.ValidationError("User is not Active")
            return super(UserLoginForm, self).clean(*args, **kwargs)
        return redirect('/invalid')
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email')
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
    mobile_number = forms.CharField(min_length=10, max_length=10)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm', 'mobile_number']
    def clean(self, *args, **kwargs):
        check1 = self.cleaned_data.get('password')
        check2 = self.cleaned_data.get('password_confirm')
        if (check1 != check2):
            raise forms.ValidationError('Password must match!')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        mobile_number = self.cleaned_data.get('mobile_number')
        emailqs = User.objects.filter(email = email)
        usernameqs = User.objects.filter(username = username)
        mobile_numberqs = User.objects.filter(username=mobile_number)
        if (emailqs.exists()):
            raise forms.ValidationError('Email ID already exists')
        if(usernameqs.exists()):
            raise forms.ValidationError('Username already exists')
        if(mobile_numberqs.exists()):
            raise forms.ValidationError('Mobile number already exists')
        return super(RegisterForm, self).clean(*args, **kwargs)