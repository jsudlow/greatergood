from django.shortcuts import render
from django.views import generic
from roofy.models import Note

# Create your views here.
from django.http import HttpResponse


def roofy_notes_view(request,project_id):
	return render(request, 'roofy/notes.html',{'notes': Note.objects.all(), 'project_id':project_id} )	

def roofy_notes_test(request,project_id):
	return render(request, 'roofy/notes.html', {'notes': Note.objects.all()} )	
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class roofy_notes_generic_view(generic.ListView):
    model = Note

def roofy_add_note(request,project_id):
	return HttpResponse("You've just been redirected after adding a note")

