from django.urls import include, path
from . import views

app_name = "user"

urlpatterns = [
    path('list/', views.user_list, name="list")
]
