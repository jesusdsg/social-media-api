from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from api.models import Post
from api.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"data": serializer.data,
                    "message": 'Post created sucessfully!'}
            return Response(status=status.HTTP_201_CREATED, data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"data": serializer.data,
                    "message": 'Post created sucessfully!'}
            return Response(status=status.HTTP_201_CREATED, data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
