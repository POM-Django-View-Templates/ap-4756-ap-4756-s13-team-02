from django.shortcuts import get_object_or_404, render

from .models import Book


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
