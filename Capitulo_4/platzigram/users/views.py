"""Vista de usuarios"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

def update_profile(request):
    """Actualizacion de perfil"""
    return render(request, 'users/update_profile.html')


def login_view(request):
    """Vista de login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',{'error':'Usuario o contraseña incorrecto'})
    return render(request, 'users/login.html') 


def signup(request):
    """Vista de registro de usuario"""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Las contraseñas no son iguales'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'El usuario ya existe'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        profile = Profile(user=user)
        profile.save()
        
        return redirect('login')
    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """Vista de cerrar sesion"""
    logout(request)
    return redirect('login')