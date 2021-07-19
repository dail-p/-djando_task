from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    slug = models.SlugField(max_length=250)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


def post_directory_path(instance, filename):
    return 'post_{0}/{1}'.format(instance.id, filename)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='when_published')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    when_published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    file = models.FileField(blank=True, default='', upload_to=post_directory_path)

    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


def comment_directory_path(instance, filename):
    return 'post_{0}/comment_{1}/{2}'.format(instance.post.id, instance.id, filename)


class Comment(models.Model):
    body = models.TextField(blank=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    file = models.FileField(blank=True, default='', upload_to=comment_directory_path)

