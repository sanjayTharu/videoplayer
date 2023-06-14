from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='videos')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Playlist(models.Model):
    name=models.CharField(max_length=100)
    videos=models.ManyToManyField(Video)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    