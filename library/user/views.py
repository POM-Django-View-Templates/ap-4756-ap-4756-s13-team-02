from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def user_list(request):
    users = User.objects.all()
    return render(request, "user/user_list.html", {
        "users": users
    })

def user_info(request, id: int):
    user = User.objects.get(pk=id)
    return render(request, "user/user.html", {"user": user})