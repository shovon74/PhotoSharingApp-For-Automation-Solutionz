from django import forms
from django.contrib.auth.models import User

from .models import Album, Image


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image_title', 'image_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
