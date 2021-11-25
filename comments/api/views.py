from rest_framework.viewsets import ModelViewSet
from comments.api.serializer import CommentSerializers
from comments.models import Comment
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCrateOnly
  
class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCrateOnly]
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['created_at']
    filterset_fields = ['post']