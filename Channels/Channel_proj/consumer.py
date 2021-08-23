from channels.generic.websocket import WebsocketConsumer

class TestConsumer(WebsocketConsumer):
    def connect(self):
        pass
    def recieve(self):
        pass
    def disconnect(self, code):
        pass