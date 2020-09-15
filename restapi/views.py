from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from .models import Tag
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TagSerializer
#from rest_framework.permissions import IsAuthenticated
from .serializers import TagSerializer


#class TagListView(generics.ListAPIView):
    #permissions_classes = (IsAuthenticated,)
#    queryset = Tag.objects.all().order_by('-name')
    #serializer_class = TagSerializer

@api_view(['GET', 'POST'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tag_details(request, id):
     #try:
     #  tag = Tag.objects.get(id=id)
    #except ObjectDoesNotExist:
    #    return Response(status=status.HTTP_404_NOT_FOUND)
    tag = Tag.objects.get(id=id)
    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        