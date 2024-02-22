from analytics import service

def log_login_view(func):
    def inner(request, *args, **kwargs):
        service.log_login(request)
        return func(request, *args, **kwargs)

    return inner