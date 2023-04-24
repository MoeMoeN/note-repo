from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from braces.views import CsrfExemptMixin

from django.shortcuts import render, get_object_or_404

import logging
logger = logging.getLogger()

from .models import Note, DeletedNote, Todo
from .serializers import NoteSerializer, DeletedNoteSerializer, TodoSerializer, UserSerializer, UserInfoSerializer, LoginSerializer

class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    #Create user
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "userid": request.user.id}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)

        serializer = UserInfoSerializer(user)

        return Response(serializer.data)

class NoteAPIView(APIView):
#TO-DO zrobic authorization w headersach requestow
#aby mozna bylo np wejsc w ADD note 
#I dodac zabezpieczneie aby nie wystarczyl id note w url
#zeby nie moc odpalac notek innych uzytkownikow
    #get notes
    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        for note in notes:
            note.body = note.body[0:450] + "..." if len(note.body) > 450 else note.body
        
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)

    #create new note
    #TO-DO add limit how many notes user can create (but that's depends on user so first need to add users)
    def post(self, request):
        serializer = NoteSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class NotesDetailAPIView(APIView):
    #get note
    def get(self, request, note_id):
        note = get_object_or_404(Note, id=note_id, user=request.user.id)
        serializer = NoteSerializer(note)
        return Response(data=serializer.data)
    
    #temporaly delete
    #Todo: on delete remove note from Note model and add to Thrash model when note is deleted permanently after 30 days
    #with possibility to get this note out of thrash bin
    def delete(self, request, note_id):    
        try:
            Note.objects.filter(id=note_id, user=request.user).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    #save modified note
    def patch(self, request, note_id, format=None):
        note = get_object_or_404(Note, id=note_id, user=request.user) #should be NO_CONTENT but that's seems cleaner
        # try:
        #    note = Note.objects.get(id=note_id)
        #    return Response(status=status.HTTP_200_OK)
        # except Note.DoesNotExist:
        #     return Response(status=status.HTTP_204_NO_CONTENT)
        
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class DeletedNoteAPIView(APIView):
#TO-DO zrobic authorization w headersach requestow
#aby mozna bylo np wejsc w ADD note 
#I dodac zabezpieczneie aby nie wystarczyl id note w url
#zeby nie moc odpalac notek innych uzytkownikow
    #get notes
    def get(self, request):
        deleted_notes = DeletedNote.objects.filter(user=request.user)
        for note in deleted_notes:
            note.body = note.body[0:450] + "..." if len(note.body) > 450 else note.body
        
        serializer = DeletedNoteSerializer(deleted_notes, many=True)

        return Response(serializer.data)

class DeletedNoteDetailAPIView(APIView):

    def delete(self, request, note_id):    
        try:
            DeletedNote.objects.filter(id=note_id, user=request.user).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)