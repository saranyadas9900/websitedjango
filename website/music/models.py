from django.db import models

# Create your models here
class Album(models.Model):
    artist=models.CharField(max_length=100)
    album_title=models.TextField(max_length=500)
    genre=models.CharField(max_length=150)
    album_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self .album_title+'-'+self.artist

class song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=100)
    is_favourite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title+'-'+str(self.album)