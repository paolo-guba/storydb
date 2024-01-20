# ideas/models.py
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=100)
    creation_timeline = models.CharField(max_length=100)
    story_timeline = models.CharField(max_length=100)
    plot = models.TextField()
    # Add more fields as needed


class Character(models.Model):
    name = models.CharField(max_length=50)
    # Add more fields as needed
