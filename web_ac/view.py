from rest_framework import viewsets, generics
from api.models import *
from web_ac.serializers import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class UserList(generics.ListCreateAPIView):

    serializer_class = SkillSerializer

    def get_queryset(self):
        print(self.kwargs['id'])
        queryset = Skill.objects.filter(userId=self.kwargs['id'])
        return queryset
