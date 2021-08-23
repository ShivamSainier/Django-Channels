from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name="test_consumer"
        self.room_group_name="test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.room_group_name)
        self.accept()
        text_data=json.dumps({'status':'connected'})
        self.send(text_data)

    def receive(self,text_data):
        print(text_data)
        text_data=json.dumps({'status':'Revieved'})
        self.send(text_data)
        pass
    def disconnect(self):
        pass