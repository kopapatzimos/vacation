
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from vacation_portal.forms import VacationRequestForm
from .models import VacationRequest
from django.utils import timezone

@login_required
def submit_vacation_request(request):
    if request.method == "POST":
        form = VacationRequestForm(request.POST)
        if form.is_valid():
            # Set the manager (if selected)
            manager = form.cleaned_data['manager'] or request.user  # Default to the logged-in user if no manager is selected

            # Create a new VacationRequest instance and save it
            vacation_request = VacationRequest(
                user=request.user,
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                reason=form.cleaned_data['reason'],
                submitted_date=timezone.now(),
                status="Pending",
                manager=manager
            )
            vacation_request.save()
            return redirect('dashboard')  # Redirect to dashboard after submission
    else:
        form = VacationRequestForm()

    return render(request, 'request_leave.html', {'form': form})
  


def sign_up(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')

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
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),  # Hash the password
            )
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect("login")

    return render(request, "signup.html")



@login_required
def dashboard_view(request):
    # Dummy data for now; replace with database queries
    vacation_requests = [
        {"submitted_date": "2024-12-20", "start_date": "2025-01-10", "end_date": "2025-01-15", "status": "Approved"},
        {"submitted_date": "2024-12-15", "start_date": "2025-02-01", "end_date": "2025-02-05", "status": "Pending"},
    ]
    context = {
        "vacation_requests": vacation_requests,
    }
    return render(request, "dashboard.html", context)




