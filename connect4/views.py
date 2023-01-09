from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import Connect4Serializer
from .models import Connect4
from rest_live.mixins import RealtimeMixin

class Connect4List(generics.ListCreateAPIView, RealtimeMixin):
    queryset = Connect4.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = Connect4Serializer # tell django what serializer to use

    # websocket view
    def get_queryset(self):  # Actual queryset for the view
        return Connect4.objects

class Connect4Detail(generics.RetrieveUpdateDestroyAPIView, RealtimeMixin):
    queryset = Connect4.objects
    serializer_class = Connect4Serializer

class FilteredConnect4List(generics.ListCreateAPIView, RealtimeMixin):
    queryset = Connect4.objects.none() # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = Connect4Serializer # tell django what serializer to use

    def get_queryset(self):  # Actual queryset for the view
        return Connect4.objects.filter(user=self.request.user)