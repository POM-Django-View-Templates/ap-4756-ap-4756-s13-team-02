from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Author


def admin_check(user):
    return user.is_superuser or user.is_staff


@user_passes_test(admin_check)
def author_list(request: HttpRequest) -> HttpResponse:
    authors = Author.objects.all()
    return render(request, "author/author_list.html", {
        "authors": authors
    })


@user_passes_test(admin_check)
def author_create(request: HttpRequest) -> HttpResponse:
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    patronymic = request.POST.get("patronymic")

    if not Author.create(name, surname, patronymic):
        messages.error(request, "Invalid creation data")

    return author_list(request)


@user_passes_test(admin_check)
def author_delete(request: HttpRequest, id: int) -> HttpResponse:
    author = Author.objects.get(pk=id)
    if author.books.count() != 0:
        messages.error(request, "Delete the author's books first")
    else:
        author.delete()
    return author_list(request)


# @user_passes_test(admin_check)
# def author_books(request: HttpRequest, id: int) -> HttpResponse:
#     return render(request, "books/book_list", {"search_author": id})