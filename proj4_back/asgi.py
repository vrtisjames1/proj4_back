"""
ASGI config for proj4_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj4_back.settings')
import django
django.setup()
application = get_asgi_application()


from channels.auth import AuthMiddlewareStack
from django.urls import path
from rest_live.routers import RealtimeRouter
from connect4.views import Connect4List
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
router = RealtimeRouter()
router.register(Connect4List)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
    URLRouter([
        path("ws/subscribe/", router.as_consumer().as_asgi(), name="subscriptions"),
    ])
),
})