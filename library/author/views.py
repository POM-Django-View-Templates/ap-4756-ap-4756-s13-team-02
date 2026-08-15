from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Author


def admin_check(user):
    return user.is_superuser or user.is_staff


@user_passes_test(admin_check)
def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    return render(request, "user/user_list.html", {
        "authors": authors
    })


@user_passes_test(admin_check)
def author_info(request: HttpRequest, id: int) -> HttpResponse:
    author = Author.objects.get(pk=id)
    return render(request, "user/user.html", {"author": author})
