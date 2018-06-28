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

def find_user_id(kwargs):
    querysetSkill = Skill.objects.filter(type=kwargs['type'])
    list_skill = []
    for SkillType in querysetSkill.values('userId'):
        list_skill.append(SkillType['userId'])
    return list_skill

def find_user_id_by_note(kwargs):
    list_skill = find_user_id(kwargs)
    querysetSkill = Skill.objects.filter(userId__in=list_skill,
                                         note=kwargs['note'])
    list_skill = []
    for SkillType in querysetSkill.values('userId'):
        list_skill.append(SkillType['userId'])
    return list_skill

class UserListByType(generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        list_id_by_skill = find_user_id(self.kwargs)
        queryset = User.objects.filter(pk__in=list_id_by_skill)
        if (len(queryset) == 0):
            return None
        return queryset

class UserListByTypeAndNote(generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        list_id_by_skill = find_user_id_by_note(self.kwargs)
        queryset = User.objects.filter(pk__in=list_id_by_skill)
        if (len(queryset) == 0):
            return None
        return queryset
