from django.shortcuts import render
from .models import Note

def notes_list_view(request):
    notes = Note.objects.all()
    context = {
        'notes_list': notes,
    }
    return render(request, 'notes/note_list.html', context)
