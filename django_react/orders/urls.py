from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router1 = DefaultRouter()

router1.register("orders", OrderViewSet, basename="orders")
urlpatterns = [
    path("api/", include(router1.urls)),
]
