from rest_framework import serializers
from .models import TextEntry

class TextEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEntry
        fields = ['id', 'title', 'content', 'date_created']
