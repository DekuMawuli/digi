from django.shortcuts import render
from .models import Branch, BranchBuses, BusSeat, Bus, Driver
from .booker_decorators import regular_user_only, branch_admin_only, terminal_admin_only, auth_user_only, check_role


@auth_user_only
@check_role
@regular_user_only
def dashboard(request):
    return render(request, 'booker/regular/dashboard.html')


@auth_user_only
@terminal_admin_only
def terminal_admin_dashboard(request):
    return render(request, "booker/terminal-admin/dashboard.html")


@auth_user_only
@branch_admin_only
def branch_admin_dashboard(request):
    return render(request, "booker/branch-admin/dashboard.html")