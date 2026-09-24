from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Course
# Create your views here.

def dashboard(request):
    if request.user.is_superuser:
        role = "admin"

    elif request.user.groups.filter(name="Teacher").exists():
        role = "teacher"

    elif request.user.groups.filter(name="Student").exists():
        role = "student"

    else:
        role = "unknown"

    return render(request, "dashboard.html", {"role": role})

def course_list(request):
    courses = Course.objects.all()

    return render(request, "courses.html", {
        "courses": courses
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid username or password."
        })

    return render(request, "login.html")