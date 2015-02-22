from rest_framework import serializers
from support_ticket.models import Ticket
from support_user.models import User


class UserSerializer(serializers.ModelSerializer):
    # tickets = serializers.HyperlinkedRelatedField(many=True, view_name='ticket-list', read_only=True)
    ticket_list = serializers.ReadOnlyField(source='ticket.title')

    class Meta:
        model = User
        fields = ('username', 'ticket_list', 'company', 'image', 'about', 'phone',
        'alt_phone')
        # read_only_fields = ('username',)


class TicketSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    # owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Ticket
        fields = ('title', 'description', 'reference_url', 'owner', 'priority',
                  'status', 'date_created', 'last_modified')
        read_only_fields = ('owner', 'date_created')

