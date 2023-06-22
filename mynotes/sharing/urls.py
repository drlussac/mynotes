from django.urls import path
from . import views

app_name = "sharing"

urlpatterns = [
    path("share_note/<int:note_id>/", views.share_note, name="share_note"),
    path("shared_notes/", views.shared_notes, name="shared_notes"),
    path(
        "shared-note/<int:shared_note_id>/",
        views.view_shared_note,
        name="view_shared_note",
    ),
]
