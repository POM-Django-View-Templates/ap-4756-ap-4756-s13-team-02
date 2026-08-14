from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.contrib import messages


User = get_user_model()


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Both fields are required")
            return render(request, "authentication/login.html")
        
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                messages.success(request, f"Logged in as {email}")
                return redirect("home")
        except User.DoesNotExist:
            pass

        messages.error(request, "Invalid email or password")
        return render(request, "authentication/login.html")

    return render(request, "authentication/login.html")


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        extra_fields = {
            "first_name": request.POST.get("fname"),
            "last_name": request.POST.get("lname"),
            "middle_name": request.POST.get("mname"),
            "is_active": True,
        }

        if not email or not password:
            messages.error(request, "Both fields are required")
            return render(request, "authentication/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "User already exists")
            return render(request, "authentication/register.html")

        user = User.objects.create_user(email, password, **extra_fields)
        login(request, user)
        messages.success(request, f"Logged in as {email}")
        return redirect("home")

    return render(request, "authentication/register.html")


def logout_view(request):
    logout(request)
    messages.success(request, f"Logged out")
    return redirect("home")