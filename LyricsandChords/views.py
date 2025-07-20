from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Song
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'LyricsandChords/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        pssword2 = request.POST['password2']
        user = authenticate(request, username=username, password=password1)
        if user:
            login(request, user)
            return redirect('song_list')
    return render(request, 'LyricsandChords/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'LyricsandChords/song_list.html', {'songs': songs})