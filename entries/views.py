from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TextEntry, GeneratedPost
from .serializers import TextEntrySerializer, GeneratedPostSerializer
import openai
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class TextEntryViewSet(viewsets.ModelViewSet):
    queryset = TextEntry.objects.all()
    serializer_class = TextEntrySerializer

    # Custom action to generate a social media post
    @action(detail=True, methods=['post'])
    def generate_post(self, request, pk=None):
        text_entry = self.get_object()
        prompt = f"Generate a social media post for this text:\n\n{text_entry.content}"
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Use the appropriate model
                messages=[
        {"role": "system", "content": "You are an expert in social media marketing."},
        {
            "role": "user",
            "content": prompt
        }
    ],
                max_tokens=50
            )
            post_content = response['choices'][0]['text'].strip()

            # Save the generated post
            generated_post = GeneratedPost.objects.create(
                text_entry=text_entry,
                post_content=post_content,
                demographic_recommendation="General audience"
            )
            serializer = GeneratedPostSerializer(generated_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
