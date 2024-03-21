from django.shortcuts import render
from .models import Message, Chat
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import logout


def welcome_view(request):
    """
    This view displays the main page.
    """
    return render(request, "main/welcome.html")

@login_required
def index(request):
    """
    This view displays the chatroom.
    Users must be logged in to access this view.
    Users can input and send messages, and the sent messages will be displayed in the chatroom.
    """
    if request.method == "POST":
        print("received data " + request.POST["textmessage"])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(
            text=request.POST["textmessage"],
            chat=myChat,
            author=request.user,
            receiver=request.user,
        )
        serialized_obj = serializers.serialize("json", [new_message])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, "chat/index.html", {"messages": chatMessages})


def login_view(request):
    """
    This view allows users to log in.
    Upon successful login, they will be redirected to the chat page.
    """
    redirect = request.GET.get("next", "/chat/")
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get("redirect"))
        else:
            return render(
                request,
                "auth/login.html",
                {"wrongPassword": True, "redirect": redirect},
            )
    return render(request, "auth/login.html", {"redirect": redirect})

def logout_view(request):
    """
    This view allows users to log out.
    After logging out, they will be redirected to the login page.
    """
    logout(request)
    return HttpResponseRedirect("/login/") 

def register_view(request):
    """
    This view allows users to register.
    They can input a username and password.
    Upon successful registration, they will be redirected to the specified redirection page.
    """
    redirect = request.GET.get("next", "/chat/")
    password = request.POST.get("password")
    checkPassword = request.POST.get("checkPassword")
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if password == checkPassword:
            user.save()
            login(request, user)
            return HttpResponseRedirect(request.POST.get("redirect"))
        else:
            return render(request, "auth/login.html", {"redirect": redirect})

    return render(request, "register/register.html", {"redirect": redirect})
