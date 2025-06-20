from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AgressorViewSet,
    AssistidaViewSet,
    GuarnicaoIntegranteViewSet,
    GuarnicaoViewSet,
    LoginAPI,
    PolicialViewSet,
)

router = DefaultRouter()
router.register(r"policiais", PolicialViewSet)
router.register(r"guarnicoes", GuarnicaoViewSet, basename="guarnicao")
router.register(r"agressores", AgressorViewSet, basename="agressor")
router.register(r"assistidas", AssistidaViewSet, basename="assistida")
router.register(
    r"guarnicoes_integrantes",
    GuarnicaoIntegranteViewSet,
    basename="guarnicoes_integrantes",
)

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="login_api"),
    path("", include(router.urls)),
]
