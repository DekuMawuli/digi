from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("sign-out/", views.sign_out, name="sign_out"),
    path("process-login/", views.process_login, name="process_login")
]
