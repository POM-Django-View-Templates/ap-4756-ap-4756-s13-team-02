from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

User = get_user_model()


def user_list(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, "user/user_list.html", {"users": users})


def user_info(request: HttpRequest, id: int) -> HttpResponse:
    user = User.objects.get(pk=id)
    return render(request, "user/user.html", {"user": user})
