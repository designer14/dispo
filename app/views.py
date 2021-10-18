from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import User, Post
from .serializers import UserSerializer, PostSerializer, GetUserSerializer, GetPostSerializer

@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_post(request):
     serializer = PostSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_user(request):
#     snippets = User.objects.all()
    snippets = User.objects.annotate(numPost=Count('posts')).order_by('-numPost')
    serializer = GetUserSerializer(snippets, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_post(request, user_id):
    snippets = Post.objects.filter(user=user_id).order_by('-timestamp')
    serializer = GetPostSerializer(snippets, many=True)
    return Response(serializer.data)
