from django.urls import path

from .views import NoteAPIView, NotesDetailAPIView

urlpatterns = [
    path('notes/', NoteAPIView.as_view(), name='notes'),
    path('notes/<uuid:note_id>/', NotesDetailAPIView.as_view(), name='note-detail'),
]