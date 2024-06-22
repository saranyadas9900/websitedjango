from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from.models import Album
# Create your views here.

def index(request):
    all_albums=Album.objects.all()
    context={
        'album1':all_albums
    }
    return render(request,'music/index.html',context)
def details(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/details.html',{'album2':album})       