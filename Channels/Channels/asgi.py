"""
ASGI config for Channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from Channels.settings import WSGI_APPLICATION
import os
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from Channel_proj.consumer import TestConsumer
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Channels.settings')

application = get_asgi_application()

ws_patterns=[
    path('ws/test/',TestConsumer.as_asgi())
]

application=ProtocolTypeRouter(
    {
        'websocket':URLRouter(ws_patterns)
    }
)
