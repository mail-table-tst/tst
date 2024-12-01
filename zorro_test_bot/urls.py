from django.urls import path
from .views import index, handle_bot_request, poll_updates, ws

urlpatterns = [
    path('', index),
    path('ws/', ws),
    path('update/', handle_bot_request),
    path('poll/', poll_updates)
]
