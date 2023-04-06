from rest_framework import serializers
from .models import Note, Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Todo
        fields = (
            'id',
            'title',
            'body',
            'deadline',
        )

class NoteSerializer(serializers.ModelSerializer):
    
    todos = TodoSerializer(many=True)
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'body',
            'todos',
            'user',
            'created',
        )
