from rest_framework import routers
from analytics.viewsets import UserActivityViewSet, LikeAnalyticsViewSet

router = routers.DefaultRouter()
router.register('user-activity', UserActivityViewSet, basename='user-activity')
router.register('like-analytics', LikeAnalyticsViewSet, basename='like-analytics')


urlpatterns = [
    *router.urls,
]