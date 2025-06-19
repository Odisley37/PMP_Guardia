from django.urls import path

from .views import HelloAPI, LoginAPI

urlpatterns = [
    path("hello/", HelloAPI.as_view(), name="hello_api"),
    path("login/", LoginAPI.as_view(), name="login_api"),
]
