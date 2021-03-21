from django.shortcuts import render
from django.http import JsonResponse


from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import PostSerializer
from blog.models import Post


class PostView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""
class test_view(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
"""

# Create your views here.
# def test_view(request):
#    data = {
#        'name': 'try',
#        'age': 25
#    }
#    return JsonResponse(data)
