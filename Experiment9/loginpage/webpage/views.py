# loginpage/webpage/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def HomeView(request):
    return render(request, 'home.html')

def register(request):  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()  
            login(request, user)
            return redirect('/home/')
        else:
            context = {'messages': ['There was an error']}
            return render(request, 'register.html', context)
  
    else:  
        form = UserCreationForm()  
        context = { 'form':form }  
        return render(request, 'register.html', context)