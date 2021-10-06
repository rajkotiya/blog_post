
from django.urls import path, include
from django.conf import settings
from graphene_django.views import GraphQLView
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

