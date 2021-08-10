from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group,User
from .models import Room,Group_Message

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
    message = request.POST['message']
    room_name = request.POST['roomName']
    # print("====== in the send function ====")
    # print("all the data is in the game of the adsfkn alskdf",message,room_name)
    username=request.user.username
    # print(username)
    new_message = Group_Message.objects.create(value=message,group_id=room_name,user=username)
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
    print("in the get messages ========== =+++++")
    username=request.user.username
    print("this is the user name=====++++ ",username )
    messages = Group_Message.objects.filter(group_id=room_name)
    # print(messages.user)
    return JsonResponse({"messages":list(messages.values()),"username":username})


def removeuser(request,room_name):
    print("in the remove user url")
    group = Group.objects.get(name=room_name)
    user=request.user
    user.groups.remove(group)
    return redirect('/group/')