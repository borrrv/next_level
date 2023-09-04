from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ContactsViewSet

router = DefaultRouter()

router.register("contacts", ContactsViewSet)

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("", include(router.urls)),
]
