from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Message
from .serializers import MessageSerializer


# Create your views here.
def index(request):
    context = {}
    return render(request, "chat/index.html", context)

def room(request, room_name):
    context={'room_name': room_name}
    return render(request, "chat/room.html", context)

@api_view(["GET"])
def getLastTenMessages(request):
    messages = Message.last_10_messages()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)