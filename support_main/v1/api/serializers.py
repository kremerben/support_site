from rest_framework import serializers
from support_ticket.models import Ticket
from support_user.models import User


class UserSerializer(serializers.ModelSerializer):
    # tickets = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     lookup_field='owner',
    #     view_name='ticket-detail'
    # )
    # ticket_list = serializers.HyperlinkedIdentityField(view_name='ticket-list')
    tickets = serializers.ReadOnlyField(source='ticket.title')
    # tickets = TicketSerializer(many=True)
    # tickets = serializers.HyperlinkedRelatedField(many=True)

    class Meta:
        model = User
        fields = ('username', 'tickets', 'company', 'image', 'about', 'phone',
        'alt_phone')
        # read_only_fields = ('username',)


class TicketSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    # owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Ticket
        fields = ('title', 'description', 'reference_url', 'owner', 'priority',
                  'status', 'date_created', 'last_modified')
        # read_only_fields = ('owner', 'date_created')

