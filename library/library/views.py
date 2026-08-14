from django.shortcuts import render
from django.contrib import messages


def home(request):
    messages.info(request, request.user.username)
    return render(request, "base.html")
