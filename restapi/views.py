from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers

from .models import Tag
from rest_framework import viewsets, generics
#from rest_framework.permissions import IsAuthenticated
from .serializers import TagSerializer


class TagListView(generics.ListAPIView):
    #permissions_classes = (IsAuthenticated,)
    queryset = Tag.objects.all().order_by('-name')
    serializer_class = TagSerializer