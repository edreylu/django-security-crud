from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "register/passwordchange.html", {"form":form})