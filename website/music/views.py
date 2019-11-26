from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

def index(request):
	all_album = Album.objects.all()
	context = {
		'all_album' : all_album,
	}
	return render(request, 'music/index.html', context)

def details(request, id):
	return HttpResponse("<h1>The ID is : "+ str(id) +"</h1>")