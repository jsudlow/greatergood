from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def roofy_notes_view(request,project_id):
	return render(request, 'roofy/notes.html')

def roofy_notes_test(request,project_id):
	return render(request, 'roofy/notes.html')	
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

