"""web_ac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .view import *

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('project', ProjectViewSet)
router.register('skill', SkillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/<int:id>/skill', UserList.as_view(),name='user-list'),
    path('user/skill/<str:type>', UserListByType.as_view(),name='userbyType-list'),
    path('user/skill/<str:type>/<str:note>',
         UserListByTypeAndNote.as_view(),name='userbyTypeAndNote-list'),
]
