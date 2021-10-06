from channels.generic.websocket import WebsocketConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


class DeniedConsumer(WebsocketConsumer):
    def connect(self):
        self.close()


class OkConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send("OK")
        self.close()


websocket_urlpatterns = [
    path("ws/denied/", DeniedConsumer.as_asgi()),
    path("ws/ok/", OkConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
