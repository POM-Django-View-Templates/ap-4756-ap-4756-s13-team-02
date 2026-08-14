from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:id>/", views.book_detail, name="book_detail"),
    path("<int:id>/edit", views.book_edit, name="book_edit"),
    path("<int:id>/delete", views.book_delete, name="delete_book"),
    path("<int:id>/update/", views.book_update, name="book_update"),
]
