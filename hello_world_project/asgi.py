import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from hello_world.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP Requests
    "websocket": AuthMiddlewareStack(  # WebSocket Requests
        URLRouter(websocket_urlpatterns)
    ),
})
