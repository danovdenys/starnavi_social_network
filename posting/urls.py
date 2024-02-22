from rest_framework import routers

from posting.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    *router.urls,
]