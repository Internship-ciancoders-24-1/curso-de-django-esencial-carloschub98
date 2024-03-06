#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#modelos
from posts.models import Post

#forms
from posts.forms import PostForm

#Utilidades
from datetime import datetime

# Create your views here.

@login_required
def list_posts(request):
    """Listado de posts"""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts':posts})

@login_required
def create_post(request):
    """Crear un post"""
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
                        
            return redirect('feed')
    else:
        form = PostForm()
    
    return render(
        request =request,
        template_name='posts/new.html',
        context = {
            'profile': request.user.profile,
            'user': request.user,
            'form': form
        }
    )
