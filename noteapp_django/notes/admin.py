from django.contrib import admin
from .models import Note, DeletedNote, Todo
# Register your models here.
admin.site.register(Note)
admin.site.register(DeletedNote)
admin.site.register(Todo)