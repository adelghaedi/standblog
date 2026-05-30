from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, UserEditForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home:index")

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = User.objects.get(username=login_form.cleaned_data.get("username"))
            if user is not None:
                login(request, user)
                return redirect("home:index")
    else:
        login_form = LoginForm()
    return render(request, "account/login.html", context={"form": login_form})


def logout_view(request):
    logout(request)
    return redirect("home:index")


def register_view(request):
    password_not_match_error = None
    confirm_password = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            password = form.cleaned_data.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                password_not_match_error = "Passwords don't match"
            else:
                user = form.save()
                login(request, user)
                return redirect("home:index")
    else:
        form = RegisterForm()

    return render(
        request,
        "account/register.html",
        {
            "form": form,
            "confirm_password": confirm_password,
            "password_not_match_error": password_not_match_error
        }
    )


def edit_view(request):
    user = request.user

    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = UserEditForm(instance=user)

    return render(request,"account/edit.html",{"form":form})