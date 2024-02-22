from django.apps import apps
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from analytics.models import UserActivity
from analytics.serializers import LikeActivitySerializer, UserActivitySerializer

from django.db.models.functions import TruncDate
from django.db.models import Count

class UserActivityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated | IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return UserActivity.objects.all()
        return UserActivity.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def last_activity(self, request, *args, **kwargs):
        user = request.user
        last_activity = UserActivity.objects.filter(user=user).order_by('-date').first()
        last_login = UserActivity.objects.filter(user=user, activity='login').order_by('-date').first()
        return Response(status=200, data={
            'user': user.username,
            'last_request': self.get_serializer(last_activity).data,
            'last_login': self.get_serializer(last_login).data
        })


class LikeAnalyticsViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = LikeActivitySerializer
    # permission_classes = [IsAuthenticated | IsAdminUser]
    
    def get_queryset(self):
        '''Get the daily number of likes for the user.'''
        # user = request.user
        LikeModel = apps.get_model('posting.Like')
        likes = LikeModel.objects.all()
        # if not user.is_staff:
        #     likes = likes.filter(user=user)
        
        return likes.annotate(date=TruncDate('date_liked'))
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.values('date').annotate(count=Count('id')).values('date', 'count')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
