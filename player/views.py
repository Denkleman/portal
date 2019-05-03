from django.shortcuts import render
from django.http import HttpResponse
from .forms import  UserRegisterForm
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def team(request):
    return render(request, 'player/team.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'player/register.html', {'form': form})

