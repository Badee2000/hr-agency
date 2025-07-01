from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chats.urls')),
]


# In Pruduction
# def redirect_to_admin(request, exception):
#     return redirect('/admin/')


# handler404 = 'system.urls.redirect_to_admin'
