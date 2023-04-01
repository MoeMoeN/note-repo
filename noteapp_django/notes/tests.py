from django.test import TestCase
from .models import Note, Todo
from django.contrib.auth.models import User
# Create your tests here.
class NoteTests(TestCase):

    def testCreateShortNoteWithTodo(self):
        user = User.objects.create_user(username='35testusersd', password='12345dds')

        title = "safagdsgdsdcv"
        body = "jksanfbkasbkfas"

        note = Note(title=title, body=body, user=user)

        note.save()

        ntitle = "todotitle"
        nbody = "todo\nbody\nhefsghe"
        
        todo = Todo(note=note, title=ntitle, body=nbody)
        todo.save()
    def testCreateEmptyNote(self):
        user_id = User.objects.create_user(username='35testusersd', password='12345dds')

        title = ''
        body = ''

        note = Note(title=title, body=body, user=user_id)

        note.save()

    def testCreateLongNote(self):
        user_id = User.objects.create_user(username='35testusersd', password='12345dds')

        title = 'jnkasfjhifhiafh9a9395h9t3529fe9f29nf23253526'
        body = 't32000ae0gfw0n3ajh0fajf3j0aj0a3j0f0jax0j\nafnmfasdnfnakfjnkafnua9fah9f9a\
        fasjklnlm,asm,ndandnksknjdsajkndsjknsdjnkakjafnlfanklflknas\
            jksdakdjkasjkdsjkasdjkdsajkajdksjkdasjkdasjkasdjkjkads\
                jksakjdsakjdjknsajkndsaaaaaaaaaaaaaaaaaaaaaasdkjvna9hf93h93r2h94539h3529h5h923h9r23h95h25390h902u390uv2390v29nu33v9u0v9u229u039un2v53u9n2v3n9vn9u329nvu92n0u9nu0vn9u3v2nu9as0hrf90ahg90dangad9u0gndg90\
                    8nfas8nfanrn93uan9ufan9ufnu93anu9fnau9nsu9dfna9unf903n90fna9fn39a0nf90a3n9fna9fn9a03nfan9fna90nf39anf93na9fn9a0nf9an9f3n9a3nf9a3n9fn3a9fn9anf93an9fna9fna9nf9na9fn93n9anf9a3nf9na9fn9a3nf9na39fn93afn9a3nf9anfna9nf9an9fna90fn9fna90nf'

        note = Note(title=title, body=body, user=user_id)

        note.save()
    
