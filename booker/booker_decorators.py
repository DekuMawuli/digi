from django.shortcuts import redirect
from django.contrib import messages

# from .models import Branch, BranchBuses, BusSeat, Bus, Driver


def auth_user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("users:login_user")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("booker:dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def check_role(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == 2:
            return redirect("booker:station_admin")
        elif request.user.role == 3:
            return redirect("booker:branch_admin")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def regular_user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role != 1:
            messages.warning(request, "You are not Permitted to See the requested Page")
            return redirect("booker:dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def terminal_admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role != 2:
            messages.warning(request, "You are not Permitted to See the requested Page")
            return redirect("booker:station_admin")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def branch_admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role != 3:
            messages.warning(request, "You are not Permitted to See the requested Page")
            return redirect("booker:station_admin")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

