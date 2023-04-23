from django.urls import path

from .views import NoteAPIView, NotesDetailAPIView, DeletedNoteAPIView, CreateUserView, LoginView, LogoutView, UserView

urlpatterns = [
    path('sign-up/', CreateUserView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('notes/', NoteAPIView.as_view(), name='notes'),
    path('deleted-notes/', DeletedNoteAPIView.as_view(), name='deleted-notes'),
    path('notes/<uuid:note_id>/', NotesDetailAPIView.as_view(), name='note-detail'),
    path('user/', UserView.as_view(), name='user'),
]