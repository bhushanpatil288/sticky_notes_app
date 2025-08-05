from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note

def home(request):
    return render(request, 'notes/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

def dashboard(request):
    user_notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/dashboard.html', {'notes': user_notes})
    
@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Note.objects.create(user=request.user, title=title, content=content)
            return redirect('dashboard')
    return render(request, "notes/create_note.html")    

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note,id=note_id, user=request.user)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('dashboard')

    return render(request, "notes/edit_note.html", {'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')
    return render(request, "notes/delete_note.html", {'note':note})