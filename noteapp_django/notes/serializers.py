from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from rest_framework import serializers
from .models import Note, Todo, User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def create(self, validated_data):
        user = User(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        noteUserGroup = Group.objects.get(name='noteUser')
        user.groups.add(noteUserGroup)

        return user

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username", write_only=True)
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                raise serializers.ValidationError('Wrong username or password.', code='authorization')
        else:
            raise serializers.ValidationError('username or password is not provided', code='authorization')
        
        attrs['user'] = user
        return attrs

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
