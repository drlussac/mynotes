from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignupForm, NoteForm
from .models import Note
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    notes = Note.objects.all()
    return render(request, "notes/home.html", {"notes": notes})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    context = {"note": note}
    return render(request, "notes/note_detail.html", context)


@login_required
def display_notes(request):
    query = request.GET.get("query")
    notes = Note.objects.filter(owner=request.user)

    if query:
        notes = notes.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {"notes": notes}
    return render(request, "notes/display_notes.html", context)


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            messages.success(request, "Note created successfully.")
            return redirect("notes:display_notes")
    else:
        form = NoteForm()
    return render(request, "notes/create_note.html", {"form": form})


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect("notes:display_notes")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/edit_note.html", {"form": form, "note": note})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("notes:display_notes")
    return render(request, "notes/delete_note.html", {"note": note})


def signup(request):
    if request.user.is_authenticated:
        return redirect("notes:display_notes")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign up successful!")
            return redirect("notes:login")
    else:
        form = SignupForm()

    password_error = form.errors.get("password1")

    return render(
        request, "notes/signup.html", {"form": form, "password_error": password_error}
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("notes:home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "notes/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("notes:login")
