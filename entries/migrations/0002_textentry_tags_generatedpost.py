# Generated by Django 5.1.3 on 2024-11-15 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textentry',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='GeneratedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField()),
                ('demographic_recommendation', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_posts', to='entries.textentry')),
            ],
        ),
    ]