from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^city/city1', consumers.ChatConsumer.as_asgi()),
]
