# ideas/urls.py
from django.urls import path
from .views import StoryListCreateView, StoryDetailView

urlpatterns = [
    path('stories/', StoryListCreateView.as_view(), name='story-list-create'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
]