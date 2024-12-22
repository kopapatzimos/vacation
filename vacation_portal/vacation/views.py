
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password-confirm")
        # Validate form data
        if not email or not username or not password or not password_confirm:
            messages.error(request, "All fields are required.")
        elif password != password_confirm:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            # Create user
            User.objects.create(
                username=username,
                email=email,
                password=make_password(password),  # Hash the password
            )
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect("login")

    return render(request, "signup.html")






@login_required
def dashboard(request):
    return render(request, 'dashboard.html')