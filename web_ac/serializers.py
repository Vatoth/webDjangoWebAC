from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('firstName', 'lastName',
        'salaryClaims', 'description', 'email')
