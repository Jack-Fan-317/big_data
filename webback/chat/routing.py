from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^chat/lobby', consumers.ChatConsumer.as_asgi()),
]
