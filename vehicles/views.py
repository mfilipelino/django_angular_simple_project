from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from vehicles.serializers import UserSerializer, GroupSerializer

