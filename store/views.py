from django.shortcuts import render, redirect
from django import forms
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UpdateInfoForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect('home')
        else:
            messages.warning(request, "There was an error, please try again!")
            return redirect('login')
    else:
        return render(request, 'login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('home')



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have register sucessfully"))
            return redirect('home')
        else:
            messages.warning(request, "Opps! There was an error while register...please try again!")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    

def update_user(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateUserForm(instance=user)
        if request.method == "POST":
            form = UpdateUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, ("User has been updated successfully!"))
                return redirect('home')
            else:
                messages.warning(request, ("There was an error while updating user...please try again!"))
                return redirect('update_user')
        else:
            return render(request, 'update_user.html', {'form':form})
    else:
        messages.warning(request, ("You need to login first!"))
        return redirect('login')


def update_password(request):
    if request.user.is_authenticated:
        user = request.user
        form = ChangePasswordForm(user)
        if request.method == "POST":
            form = ChangePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Password has been updated successfully!"))
                return redirect('home')
            else:
                messages.warning(request, ("There was an error while updating password...please try again!"))
                return redirect('update_password')
        else:
            return render(request, 'update_password.html', {'form':form})
    else:
        messages.warning(request, ("You need to login first!"))
        return redirect('login')


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user=request.user)
        profile = request.user.profile
        form = UpdateInfoForm(instance=profile)
        if request.method == "POST":
            form = UpdateInfoForm(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, ("Profile has been updated successfully!"))
                return redirect('home')
            else:
                messages.warning(request, ("There was an error while updating profile...please try again!"))
                return redirect('update_info')
        else:
            return render(request, 'update_info.html', {'form':form})






def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})




def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products})
    except:
        messages.success(request, ("Category doesn't exist.."))
        return redirect('home')



def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories':categories})
    


