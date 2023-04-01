from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note, Todo
from .serializers import NoteSerializer, TodoSerializer


class NoteAPIView(APIView):

    def get(self, request):
        notes = Note.objects.all()

        for note in notes:
            note.body = note.body[0:450] + "..." if len(note.body) > 450 else note.body
        
        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else: 
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class NotesDetailAPIView(APIView):

    def get(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        serializer = NoteSerializer(note)
        return Response(data=serializer.data)
    
    def delete(self, request, note_id):
        #temporaly delete
        #Todo: on delete remove note from Note model and add to Thrash model when note is deleted permanently after 30 days
        #with possibility to get this note out of thrash bin
        Note.objects.filter(id=note_id).delete()
        return Response(status=status.HTTP_200_OK)
