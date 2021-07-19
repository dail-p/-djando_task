from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'post']


class CommentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'file')


class PostsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'comments_count', 'comments']


class PostUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'file')
