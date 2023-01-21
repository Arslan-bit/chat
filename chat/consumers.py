from django.contrib.auth.models import User
from .serializer import UserSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

class UserConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserSerializer















# from django.contrib.auth.models import User
# from .serializer import UserSerializer
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.decorators import action

# class UserConsumer(GenericAsyncAPIConsumer):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @action()
#     async def send_email(self, pk=None, to=None, **kwargs):
#         user = await database_sync_to_async(self.get_object)(pk=pk)
#         # ... do some stuff
#         # remember to wrap all db actions in `database_sync_to_async`
#         return {}, 200  # return the content and the response code.

#     @action()  # if the method is not async it is already wrapped in `database_sync_to_async`
#     def publish(self, pk=None, **kwargs):
#         user = self.get_object(pk=pk)
#         # ...
#         return {'pk': pk}, 200
    








# 1st
# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.consumers import AsyncAPIConsumer
# from rest_framework import status

# class MyConsumer(AsyncAPIConsumer):

#     @action()
#     async def an_async_action(self, some=None, **kwargs):
#         # do something async
#         return {'response with': 'some message'}, status.HTTP_RESPONSE_OK

#     @action()
#     def a_sync_action(self, pk=None, **kwargs):
#         # do something sync
#         return {'response with': 'some message'}, status.HTTP_RESPONSE_OK




























# step one advance
# consumers.py
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.mixins import (
#     ListModelMixin,
#     RetrieveModelMixin,
#     PatchModelMixin,
#     UpdateModelMixin,
#     CreateModelMixin,
#     DeleteModelMixin,
# )


# class UserConsumer(
#         ListModelMixin,
#         RetrieveModelMixin,
#         PatchModelMixin,
#         UpdateModelMixin,
#         CreateModelMixin,
#         DeleteModelMixin,
#         GenericAsyncAPIConsumer,
# ):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer






























































# chat/consumers.py
# import json

# from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = "chat_%s" % self.room_name

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat_message", "message": message}
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))