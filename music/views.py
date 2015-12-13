from django.shortcuts import render_to_response,render
from django.template import RequestContext
from .models import Song

def SpecificSong(request):
    song = Song.objects.all()
    return render(request,'music/specificsong.html', {'song':song} )