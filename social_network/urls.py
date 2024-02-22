from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('core/', include('core.urls')),
    path('posting/', include('posting.urls')),
    path('analytics/', include('analytics.urls')),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]
