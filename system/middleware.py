# To redirect to the admin panel if the requested url does not exists.
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages


class Redirect404ToAdminMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            messages.error(
                request, f'The requested page {request.path} does not exist!')
            return redirect('/admin/')
        return response
 