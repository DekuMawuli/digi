from django.shortcuts import render, redirect
from booker.booker_decorators import unauthenticated_user
from django.contrib.auth import login, logout, authenticate, PermissionDenied
from django.contrib import messages


@unauthenticated_user
def login_user(request):
    return render(request, 'users/login.html')


def sign_out(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return redirect("users:login_user")


def process_login(request):
    if request.method == "POST":
        username = request.POST['uname']
        pwd = request.POST['pwd']
        try:
            a_user = authenticate(request, username=username, password=pwd)
        except PermissionDenied:
            messages.error(request, "Invalid Credentials")
            return redirect("users:login_user")
        try:
            login(request, user=a_user)
            return redirect("booker:dashboard")
        except Exception as e:
            messages.error(request, "Invalid Credentials.. Try Again")
            return redirect("users:login_user")

    else:
        messages.error(request, "Invalid Method")
        return redirect("users:login_user")
