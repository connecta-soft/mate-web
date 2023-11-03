from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import resolve
import re


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if '/admin/' in str(request.path) and request.path != '/admin/login':
            if not request.user.is_superuser:
                return redirect('/admin/login')


class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response