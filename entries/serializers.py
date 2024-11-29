from rest_framework import serializers
from .models import TextEntry, GeneratedPost

class TextEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextEntry
        fields = ['id', 'title', 'content', 'date_created', 'tags']

class GeneratedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedPost
        fields = ['id', 'text_entry', 'post_content', 'demographic_recommendation', 'date_created']
