from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "notes"

urlpatterns = [
    path("", views.home, name="home"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
    path("notes/", views.display_notes, name="display_notes"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("create-note/", views.create_note, name="create_note"),
    path("edit-note/<int:note_id>/", views.edit_note, name="edit_note"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
    path("accounts/login/", views.user_login),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
