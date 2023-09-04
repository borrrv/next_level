from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contact.models import Contact

from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import ContactSerializer


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("first_name", "last_name")
