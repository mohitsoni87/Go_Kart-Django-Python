# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout, get_user_model
from Accounts.forms import UserLoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
def login_view(request):
    form = UserLoginForm(request.POST or None)
    return  render(request, "Accounts/Login.html", {'form': form, 'title': 'Login'})
def auth_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password=password)
        if not user:
            raise forms.ValidationError('Invaid credentials.')
        else:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return redirect('/')
    context = {'form': form, 'title': 'Register'}
    return  render(request, 'Accounts/form.html', context)
def logout_view(request):
    logout(request)
    return  redirect('/')
