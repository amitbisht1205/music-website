from code import interact
from distutils import core
from email.headerregistry import Address
from tkinter import CASCADE
from typing import cast
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
#always mak get absolute url for update and add album for reverse
class album(models.Model):
    title=models.CharField(max_length=100,help_text='album tile')
    artist=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    release=models.DateField(max_length=100)
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png','jpeg'],'allow.images')])


    def __str__(self):
        return f"album{self.title} artist{self.artist} genre{self.genre} release{self.release}"

    def get_absolute_url(self):
        return reverse('music:home')    


class song(models.Model):
    al_id=models.ForeignKey(album,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    lyricist=models.CharField(max_length=50)
    file=models.FileField(validators=[FileExtensionValidator(['mp3','aac','amr','wav'],'allow.mp3')])


    def __str__(self):
        return f"{self.title}artist{self.artist}genre{self.genre}lyricist{self.lyricist}file{self.file}"

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.al_id.id})   

class profile(models.Model):
    u_id=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png','jpeg'])])
    address=models.TextField(max_length=100)
    intrest=models.CharField(max_length=50)
    dob=models.DateField()
