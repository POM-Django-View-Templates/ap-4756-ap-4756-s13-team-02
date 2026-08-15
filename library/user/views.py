from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


User = get_user_model()


def admin_check(user):
    return user.is_superuser or user.is_staff


@user_passes_test(admin_check)
def user_list(request):
    users = User.objects.all()
    return render(request, "user/user_list.html", {
        "users": users
    })


@user_passes_test(admin_check)
def user_info(request, id: int):
    user = User.objects.get(pk=id)
    return render(request, "user/user.html", {"user": user})
