from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = "chat-index"),
    path('<str:room_name>/', views.room, name = "chat-room"),
    path('messages/load/ten/', views.getLastTenMessages, name = "chat-getten"),
]