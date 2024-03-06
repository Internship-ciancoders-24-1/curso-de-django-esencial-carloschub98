#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#Utilidades
from datetime import datetime

# Create your views here.

posts = [
    {
        'title':'Carlos Chub',
        'user': {
            'name':'Carlos Chub',
            'picture': 'https://picsum.photos/200/200/?image=10'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1'
    },
    {
        'title':'Carmen Gonzalez',
        'user': {
            'name':'Carmen Gonzalez',
            'picture': 'https://picsum.photos/200/200/?image=11'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=2'
    },
    {
        'title':'Carlos Caal',
        'user': {
            'name':'Carlos Caal',
            'picture': 'https://picsum.photos/200/200/?image=12'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=3'
    }
]

@login_required
def list_posts(request):
    """Listado de posts"""
    return render(request, 'posts/feed.html', {'posts':posts})
