from django.contrib import admin
from django.urls import path
from . import views
from .views import adduser, creategroup, groupmessages, home, index2, removeuser, room,checkview,send,getMessages,messageDetails

urlpatterns = [
    path('',home,name='group-home'),
    path('creategroup/',creategroup,name='creategroup'),
    path('messagedetails/<int:id>', messageDetails,name='message-details'),
    path('removeuser/<str:room_name>',removeuser,name='removeuser'),
    path('send/',send, name='send'),
    path('getMessages/<str:room_name>',getMessages, name='getMessages'),
    path('checkview/<str:room_name>/',checkview, name='checkview'),
    path('adduser/<str:name>/',adduser,name='adduser'),
    path('<int:id>',groupmessages,name='groupmessages'),
    path('channel/', index2, name='index'),
    path('<str:room_name>/',room, name='room'),
]
