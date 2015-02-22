from rest_framework import serializers
from support_ticket.models import Ticket
from support_user.models import User





class UserSerializer(serializers.ModelSerializer):
    # tickets = serializers.HyperlinkedRelatedField(many=True, view_name='tickets-detail', read_only=True)
    # profile =

    class Meta:
        model = User
        fields = ('username',  'company', 'image', 'about', 'phone',
        'alt_phone')
        # read_only_fields  = ()


class TicketSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    # owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Ticket
        fields = ('title', 'description', 'reference_url', 'owner', 'priority',
                  'status', 'date_created', 'last_modified')
        read_only_fields = ('owner', 'date_created')

