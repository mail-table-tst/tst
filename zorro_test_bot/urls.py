from django.urls import path
from .views import index, handle_bot_request, poll_updates

urlpatterns = [
    path('', index),
    path('update/', handle_bot_request),
    path('poll/', poll_updates)
]
