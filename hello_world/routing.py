from django.urls import re_path
from .consumers import HelloWorldConsumer

websocket_urlpatterns = [
    re_path(r'ws/hello/$', HelloWorldConsumer.as_asgi()), 
]
