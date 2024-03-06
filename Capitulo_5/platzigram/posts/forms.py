"""Formulario de post"""
# Django
from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    """Post modelo formulario."""

    class Meta:
        """Configuracion de formulario."""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')