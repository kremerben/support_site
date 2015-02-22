from rest_framework import viewsets

from support_main.v1.api.serializers import UserSerializer, TicketSerializer
from support_ticket.models import Ticket
from support_user.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer