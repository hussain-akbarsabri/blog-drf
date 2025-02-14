# Generated by Django 4.2 on 2023-06-14 11:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes_comments', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='commented_posts', through='likes_comments.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='liked_posts', through='likes_comments.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
