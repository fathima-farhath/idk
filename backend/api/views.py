from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.


# def home(request):
#     return HttpResponse("<h1><i>This is the home page</i><h1>")

class ProjectViewset(viewsets.ViewSet):
    permission_classes=[permissions.AllowAny]
    queryset=Projects.objects.all()
    serializer_class=ProjectSerializer
    
    def list(self, request):
        queryset=self.queryset
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)

    def create(self, request):
        # print(request.body)
        # print(request.data)
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("hello",status=400)
        # return Response("hello")

    def retrieve(self, request, pk=None):
        project=self.queryset.get(pk=pk)
        serializer=self.serializer_class(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        project=self.queryset.get(pk=pk)
        serializer=self.serializer_class(project,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=400)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        project=self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)

