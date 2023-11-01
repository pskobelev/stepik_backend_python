from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm
from .models import Note


def list_notes(request):
    """List text for a given user."""
    notes = Note.objects.all()
    if request.user.is_authenticated:
        users_notes = Note.objects.filter(user=request.user).order_by(
            "-created_at"
        )
        return render(request, "notes/notes.html", {"notes": users_notes})
    return render(request, "notes/notes.html", {"notes": notes})


def add_note(request):
    """add user text"""
    if request.method == "POST":
        note = request.POST["note-text"]
        if len(note) != 0:
            new_note = Note(user=request.user, text=request.POST["note-text"])
            new_note.save()
            return redirect("notes_list")

    return render(request, "notes/add_note.html")


def sign_up(request):
    """sigh up user"""
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/reg_user.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("notes_list")
        return render(request, "registration/reg_user.html", {"form": form})


def sign_in(request):  # login page
    """login page"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi {username}, welcome back!")
                return redirect("notes_list")
        messages.error(request, "Invalid username or password")

        return render(request, "registration/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect("login")
