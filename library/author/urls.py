from django.urls import path
from . import views

app_name = "author"

urlpatterns = [
    path('list/', views.author_list, name="list"),
    path('author/<int:id>/', views.author_info, name='author')
]