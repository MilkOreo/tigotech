from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from .models import Home


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            info = Home()
            info.first_name = form.data['first_name']
            info.last_name = form.data['last_name']
            info.email = form.data['email']
            info.phone = form.data['phone']
            info.desc_data = form.data['desc_data']
            info.save()
            return render(request, 'home/index.html', {'form': form})
    else:
        form = NameForm()

    return render(request, 'home/index.html', {'form': form})