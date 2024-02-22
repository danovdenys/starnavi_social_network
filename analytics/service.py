from django.apps import apps
from analytics.choices import UserActivityChoice

import logging

logger = logging.getLogger(__name__)

def log_request(request):    
    UserActivity = apps.get_model('analytics.UserActivity')
    
    UserActivity.objects.create(
        user=request.user,
        activity=UserActivityChoice.REQUEST,
        request_path=request.path
    )
    print(f'User {request.user} made a request to {request.path}')

    
    return request

def log_login(request):
    if not request.user.is_authenticated:
        return request
    
    UserActivity = apps.get_model('analytics.UserActivity')
    
    UserActivity.objects.create(
        user=request.user,
        activity=UserActivityChoice.LOGIN,
        request_path=request.path
    )
    
    return request