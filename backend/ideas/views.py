from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Story
from .serializers import StorySerializer

class StoryListCreateView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

class StoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer