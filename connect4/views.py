from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import Connect4Serializer
from .models import Connect4

class Connect4List(generics.ListCreateAPIView):
    queryset = Connect4.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = Connect4Serializer # tell django what serializer to use

class Connect4Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Connect4.objects.all().order_by('id')
    serializer_class = Connect4Serializer