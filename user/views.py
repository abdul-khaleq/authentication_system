from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = forms.RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')
    else:
        signup_form = forms.RegistrationForm()
    return render(request, 'signup.html', {'form': signup_form})

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Your username & password did not match')
                return redirect('signup')

    login_form = AuthenticationForm()
    return render(request, 'signup.html', {'form' : login_form})

def pass_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': pass_form})

def pass_change2(request):
    if request.method == 'POST':
        pass_form = SetPasswordForm(request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, pass_form.user)
            return redirect('profile')
    else:
        pass_form = SetPasswordForm(user=request.user)
    return render(request, 'pass_change.html', {'form': pass_form})
    
def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('homepage')