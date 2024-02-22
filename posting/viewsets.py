from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from posting.models import Post
from posting.serializers import PostSerializer
from core.permissions import IsAuthorOrReadOnly, AllowCreateOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly | (AllowCreateOnly & IsAuthenticated)]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post: 'Post' = self.get_object()
        post.likes.add(request.user)
        return Response(status=200)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post: 'Post' = self.get_object()
        post.likes.remove(request.user)
        return Response(status=200)
    
    