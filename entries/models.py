from django.db import models

class TextEntry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    # "fiction", "non-fiction", "poetry", "other"
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class GeneratedPost(models.Model):
    # text_entry: Foreign key linking the post to a specific TextEntry.
    text_entry = models.ForeignKey(TextEntry, on_delete=models.CASCADE, related_name='generated_posts')
    post_content = models.TextField()
    demographic_recommendation = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post for {self.text_entry.title}"

