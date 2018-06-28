from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = User
        fields = ('id', 'firstName', 'lastName',
        'salaryClaims', 'description', 'email')

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Skill
        fields = ('id', 'name', 'userId',
                  'type', 'note')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Project
        fields = ('name', 'descriptive',
                  'id')
