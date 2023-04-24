from django.core.management.base import BaseCommand, CommandError
from notes.models import DeletedNote

from datetime import timedelta
from django.db.models.functions import Now

class Command(BaseCommand):
    help = "set expired flag to True on DeletedNote model"

    def add_arguments(self, parser):
        parser.add_argument('days', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Permanently delete expired notes'
            )
        
    def handle(self, *args, **options):
            try:
                notes_to_be_expired = DeletedNote.objects.filter(deleted__lte=Now()-timedelta(days=options['days']))
            except DeletedNote.DoesNotExist:
                 raise CommandError("There's no expired notes.")

            notes_to_be_expired.update(expired=True)

            if options['delete']:
                notes_to_be_expired.delete()

                self.stdout.write(
                    self.style.SUCCESS('Successfully deleted objects')
                )
            else:                    
                self.stdout.write(
                    self.style.SUCCESS('Successfully set expired flags')
                )
