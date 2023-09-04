from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ContactsViewSet

router = DefaultRouter()

router.register("contacts", ContactsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
