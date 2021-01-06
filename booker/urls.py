from django.urls import path
from . import views

app_name = "booker"
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("terminal-admin/", views.terminal_admin_dashboard, name="station_admin"),
    path("branch-admin/", views.branch_admin_dashboard, name="branch_admin"),
]
