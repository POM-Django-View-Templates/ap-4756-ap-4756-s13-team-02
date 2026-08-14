from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book


def is_admin(user):
    return user.is_staff or user.is_superuser


def book_list(request):
    books = Book.objects.all()

    search_title = request.GET.get("title", "").strip()
    search_author = request.GET.get("author", "").strip()

    if search_title:
        books = books.filter(name__icontains=search_title)
    if search_author:
        books = books.filter(authors__name__icontains=search_author)

    books = books.distinct()

    context = {
        "books": books,
        "search_title": search_title,
        "search_author": search_author,
    }
    return render(request, "book_list.html", context)


def book_detail(request, id: int):
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_detail.html", {"book": book})


@user_passes_test(is_admin)
def book_delete(request, id: int):
    if request.method == "GET":
        book = Book.get_by_id(id)
        if book:
            book.delete()
            messages.success(request, f"Book #{id} has been deleted.")
        else:
            messages.warning(request, f"Book #{id} does not exist.")
    return redirect("book:book_list")
