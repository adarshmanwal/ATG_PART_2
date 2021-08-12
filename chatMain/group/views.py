from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group,User
from .models import Room,Group_Message,Notification
import json

# Create your views here.
def home(request):
    groups=Group.objects.all()
    user=request.user
    group_name=request.user.groups.all()
    print("all the groups names are as follows",group_name)
    return render(request,'group/index.html',{'groups':groups,'user':user,'group_name':group_name})


def creategroup(request):
    if request.method=="POST":
        group_name=request.POST['Gname']
        print(group_name)
        group_name, created = Group.objects.get_or_create(name=group_name)
        return redirect('/group/')
    else:
        print("form no created ")
        redirect('creategroup')
    return render(request,'group/creategroup.html')

def adduser(request,name):
    my_group = Group.objects.get(name=name) 
    user=request.user
    my_group.user_set.add(user)
    return redirect('/group/')

def groupmessages(request,id):
    return render(request,'group/room.html', {
        'room_name': id
    })

def index2(request):
    return render(request, 'group/index2.html')

def room(request, room_name):
    print("===> C oming here ---")
    return render(request, 'group/room.html', {
        'room_name': room_name
    })
def send(request):
    data=json.loads(request.body)
    message = data['message']
    room_name = data['roomName']
    dataURL = data['dataURL']
    username=request.user.username
    print("=====>Saving ===> ", dataURL)
    new_message = Group_Message.objects.create(value=message,group_id=room_name,user=username,dataURL=dataURL)

    groupname=Group.objects.get(id=room_name)
    usernames=User.objects.filter(groups__name=groupname)
    notificationmessage="you get a message from "+str(groupname)+"by"+str(username)
    for i in usernames:
        print()
        if(str(username)!=str(i)):
            newnotificationmessage = Notification.objects.create(user=i,notification=notificationmessage)
            newnotificationmessage.save()
    new_message.save()
    return HttpResponse('Message sent successfully')

def checkview(request,room_name):
    print(room_name)
    if Room.objects.filter(name=room_name).exists():
        print("room_detains id is ",room_name)
        return redirect('/group/'+room_name)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        room_details = Room.objects.get(name=room_name)
        return render(request,'/group/'+room_name,{'room_details':room_details})
def getMessages(request,room_name):
    username=request.user.username
    messages = Group_Message.objects.filter(group_id=room_name)
    return JsonResponse({"messages":list(messages.values()),"username":username})


def removeuser(request,room_name):
    print("in the remove user url")
    group = Group.objects.get(name=room_name)
    user=request.user
    user.groups.remove(group)
    return redirect('/group/')


def messageDetails(request,id):
    res=Group_Message.objects.get(id=id)
    groupid=res.group_id
    res.delete()
    # url='/group/'+str(groupid)
    return render(request, 'group/md.html')