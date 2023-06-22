from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notes.models import Note
from .models import SharedNote
from .forms import ShareNoteForm


@login_required
def share_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)

    if request.method == "POST":
        share_with_username = request.POST.get("share_with")
        share_with_user = get_object_or_404(User, username=share_with_username)

        shared_note = SharedNote.objects.create(note=note, shared_with=share_with_user)
        shared_note.save()

        return redirect("notes:display_notes")

    return render(request, "sharing/share_note.html", {"note": note})


@login_required
def shared_notes(request):
    shared_notes = SharedNote.objects.filter(shared_with=request.user)
    return render(request, "sharing/shared_notes.html", {"shared_notes": shared_notes})


@login_required
def view_shared_note(request, shared_note_id):
    shared_note = get_object_or_404(
        SharedNote, id=shared_note_id, shared_with=request.user
    )

    return render(request, "sharing/shared_note.html", {"shared_note": shared_note})
