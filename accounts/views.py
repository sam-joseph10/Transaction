from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def landing(request):
    #print("METHOD:", request.method)
    #print("POST DATA:", request.POST)
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")
        
        print(email, password)
        try:
            user = authenticate(request, username=email, password=password)
        except User.DoesNotExist:
            user = None
        print("Authenticated User:", user)
        if user is not None:
            login(request, user)
            print("successfully logged in")
            if user.role == "CA":
                return redirect("/ca-dashboard/")
            else:
                return redirect("/customer-dashboard/")
        else:
            return render(request, "landing.html", {"error": "Invalid email or password"})

    return render(request, "landing.html")


@login_required
def ca_dashboard(request):
    return render(request, "ca_dashboard.html")


@login_required
def customer_dashboard(request):
    return render(request, "customer_dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("landing")   # redirect to landing page