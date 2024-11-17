# middleware.py
from django.shortcuts import redirect
from django.conf import settings

class AdminRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/home/') and not request.user.is_staff:
            return redirect('home')  # Chuyển hướng nếu người dùng không phải là admin
        response = self.get_response(request)
        return response
