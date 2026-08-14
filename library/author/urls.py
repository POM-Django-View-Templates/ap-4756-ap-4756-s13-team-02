from django.urls import include, path
from . import views

app_name = "author"

urlpatterns = [
    path('list/', views.author_list, name="list")
]
