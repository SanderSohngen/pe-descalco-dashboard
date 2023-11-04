from django.db import models
from users.models import User
from graduation.models import Graduation


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SongType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist, related_name='songs')
    version = models.CharField(max_length=255, blank=True, null=True)
    graduation = models.ForeignKey(
        Graduation,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    song_type = models.ForeignKey(SongType, on_delete=models.CASCADE)
    melodic = models.BooleanField(default=False)

    def __str__(self):
        version_str = f" ({self.version})" if self.version else ""
        artist_names = ', '.join(artist.name for artist in self.artists.all())
        return f"{self.name}{version_str} - {artist_names}"


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, related_name='playlists')
    day = models.DateField()
    responsible_teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.day.strftime('%d/%m/%y')}"
