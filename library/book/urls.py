from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="home"),
    path("<int:id>/", views.book_detail, name="book_detail"),
]
