from django.db import models
from .models import DeletedNote

from datetime import timedelta
from django.db.models.functions import Now

def PermanentDeleteExpiredNotes():
    notes_to_be_expired = DeletedNote.objects.filter(created__gte=Now()-timedelta(days=1))
    notes_to_be_expired.update(expired=True)
    return