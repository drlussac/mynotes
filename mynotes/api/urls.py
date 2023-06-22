from django.urls import path
from api.views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView
from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    path("api/notes/", NoteListCreateAPIView.as_view(), name="note-list-create"),
    path(
        "api/notes/<int:pk>/",
        NoteRetrieveUpdateDestroyAPIView.as_view(),
        name="note-retrieve-update-destroy",
    ),
    path("api-token-auth/", obtain_auth_token),
]
