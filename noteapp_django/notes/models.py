from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch import receiver

import uuid

from django.contrib.auth.models import User

import logging

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=True) #przy restore created jest na auto_now_add bo pewnie trzeba ustawic value tutaj przy post_created...

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        try: 
            return f"{self.title}" if len(self.title) < 25 else f"{self.title[0:25]}"
        except:
            return ''

@receiver(pre_delete, sender=Note)
def preNoteDelete(sender, instance, using, **kwargs):
    logger = logging.getLogger()
    logger.debug('note deleted')
    DeletedNote.objects.create(
        id=instance.id,
        title=instance.title,
        body=instance.body,
        user=instance.user,
        created=instance.created,
        )


class DeletedNote(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(null=True)
    class Meta:
        ordering = ('-deleted',)

    def __str__(self):
        try: 
            return f"{self.title}" if len(self.title) < 25 else f"{self.title[0:25]}"
        except:
            return ''

@receiver(pre_delete, sender=DeletedNote)
def preDeletedNoteDelete(sender, instance, using, **kwargs):
    logger = logging.getLogger()
    logger.debug('deleted note deleted')
    Note.objects.create(
        id=instance.id,
        title=instance.title,
        body=instance.body,
        user=instance.user,
        created=instance.created,
        )
    

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    note = models.ForeignKey(Note, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.title}" if len(self.title) < 25 else f"{self.title[0:20]}"