from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


def hello(request):
    return HttpResponse('hello')



class ProjectViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @extend_schema(
        summary='list all projects',
        description='you can see all lists',
        )
    def list(self, request):
        query_set = Project.objects.all()
        serializer = self.serializer_class(query_set, many = True)
        return Response(serializer.data)
    
    # Override `create` for POST
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  


    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk = pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)
    

    def update(self, request, pk=None):
        try:
            project = self.queryset.get(pk = pk)
        except Project.DoesNotExist:
            return Response({'error':'not found'})
        serializer = self.serializer_class(project, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk = pk)
        project.delete()
        return Response(status=204)
    
class StoreViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    parser_classes = [MultiPartParser, FormParser] 

    def list(self, request):
        stores = Store.objects.all()
        serializer = self.serializer_class(stores, many=True, context={'request': request})
        return Response(serializer.data)

    @extend_schema(
        summary="Upload a new project with an image",
        request={
            "multipart/form-data": StoreSerializer
        },
        responses={201: StoreSerializer},
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        try:
            store = self.queryset.get(pk=pk)
        except Store.DoesNotExist:
            return Response({'error': 'Store not found'}, status=404)
        serializer = self.serializer_class(store, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            store = self.queryset.get(pk=pk)
        except Store.DoesNotExist:
            return Response({'error': 'Store not found'}, status=404)
        serializer = self.serializer_class(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            store = self.queryset.get(pk=pk)
        except Store.DoesNotExist:
            return Response({'error': 'Store not found'}, status=404)
        store.delete()
        return Response(status=204)
