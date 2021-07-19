from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from posts.models import Post, Comment
from posts.api.serializers import *


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class PostUploadView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostUploadSerializer
    parser_classes = (FormParser, MultiPartParser, )

    def put(self, request, pk):
        if request.FILES:
            file = request.FILES
            post = self.queryset.get(id=pk)
            post.file = file.get("file")
            post.save()
            return Response(data={"status":"Success"})

        return Response(data={"status": "Error"})


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        post_id = request.POST["post"]
        post = Post.objects.get(id=post_id)
        post.comments_count = post.comments_count + 1
        post.save()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentPostView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, pk, **kwargs):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



class CommentUploadView(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUploadSerializer
    parser_classes = (FormParser, MultiPartParser, )

    def put(self, request, pk):
        if request.FILES:
            file = request.FILES
            comment = self.queryset.get(id=pk)
            comment.file = file.get("file")
            comment.save()
            return Response(data={"status":"Success"})

        return Response(data={"status": "Error"})