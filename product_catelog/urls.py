from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductListViewSet

router = DefaultRouter()
router.register(r"products", ProductListViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
