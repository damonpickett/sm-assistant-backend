from django.shortcuts import render
from rest_framework import viewsets
from .models import TextEntry
from .serializers import TextEntrySerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class TextEntryViewSet(viewsets.ModelViewSet):
    queryset = TextEntry.objects.all()
    serializer_class = TextEntrySerializer
