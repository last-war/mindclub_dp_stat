from django.shortcuts import render, redirect
from .forms import SeasonForm, GameTypeForm
from .models import Season, GameType


# Create your views here.
def main(request):
    return render(request, 'mindclubapp/index.html')


def gametype(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='mindclubapp:main')
        else:
            return render(request, 'mindclubapp/gametype.html', {'form': form})

    return render(request, 'mindclubapp/gametype.html', {'form': GameTypeForm()})


def season(request):
    gametypes = GameType.objects.all()
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='mindclubapp:main')
        else:
            return render(request, 'mindclubapp/season.html', {'form': form})

    return render(request, 'mindclubapp/season.html', {'form': SeasonForm()})

