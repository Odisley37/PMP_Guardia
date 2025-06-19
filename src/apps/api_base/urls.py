from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoginAPI, PolicialViewSet

router = DefaultRouter()
router.register(r"policiais", PolicialViewSet)

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="login_api"),
    path("", include(router.urls)),
]
