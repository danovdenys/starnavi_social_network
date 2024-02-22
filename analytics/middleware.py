from django.apps import apps
from analytics import service
from django.utils.deprecation import MiddlewareMixin

class AnalyticsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated:
            return response
        service.log_request(request)
        return response