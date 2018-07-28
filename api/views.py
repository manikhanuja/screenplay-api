from django.shortcuts import render
from api.models import Screenplay
from api.serializers import ScreenplaySerializer
from rest_framework import generics

# Create your views here.
class ScreenplayList(generics.ListCreateAPIView):
    queryset = Screenplay.objects.all()
    serializer_class = ScreenplaySerializer


class ScreenplayListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screenplay.objects.all()
    serializer_class = ScreenplaySerializer


