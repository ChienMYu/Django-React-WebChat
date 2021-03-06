#chat/consumers.py
import json 
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
#import message model so you can save it to database
from .models import Message
from .serializers import MessageSerializer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        #Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name 
        )


        self.accept()






    def disconnect(self, close_code):
        #leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name 
        )





    #Receiving message from WebSocket
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']


        
        user = User.objects.get(id=1)
        data = {
            'content':message,
            'author': 1
            }
        my_message = Message(author=user)
        serializer = MessageSerializer(my_message, data=data, many=False)
        if serializer.is_valid():
            serializer.save()


        #send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )


    #Receiving message from room group
    def chat_message(self, event):
        message = event['message']
        print(message)
        #send message to websocket 
        self.send(text_data = json.dumps({
            'message': message,
            'author': 1,
        }))