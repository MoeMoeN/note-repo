from django.db import models
import uuid
from django.contrib.auth.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        try: 
            return f"{self.title}" if len(self.title) < 25 else f"{self.title[0:25]}"
        except:
            return ''

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey(Note, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.title}" if len(self.title) < 25 else f"{self.title[0:20]}"