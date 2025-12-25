from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import  CustomUserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Voiture

def inscription(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if  form.is_valid:
            form.save()
            return render(request,'acceuil.html')
    else:
        form = CustomUserCreationForm()
    return render (request, 'inscription.html', {'form':form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('acceuil')
        else:
            messages.error(request,'Nom dutilisateur ou le mot de pass incorrect.')
    return render(request, 'connexion.html')
@login_required
def acceuil(request):
    return render(request,'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

def  list_voiture(request):
    voiture = Voiture.objects.all()
    return render (request , 'GestionVoiture/list.html', {'voiture': Voiture})