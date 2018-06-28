from rest_framework import viewsets
from api.models import User
from web_ac.serializers import *

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
