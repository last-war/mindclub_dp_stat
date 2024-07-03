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
        print(GameType.objects.get(id=request.POST.get('gametype')))
        form = SeasonForm(request.POST)
        if form.is_valid():
            new_season = form.save(commit=False)
            new_season.name = request.POST.get('name')
            new_season.gametype_id = request.POST.get('gametype')
            new_season.save()
            return redirect(to='mindclubapp:main')
        else:
            print(form.errors)
            return render(request, 'mindclubapp/season.html', {'form': form, 'gametypes': gametypes})
    return render(request, 'mindclubapp/season.html', {'form': SeasonForm(), 'gametypes': gametypes})


def quiz(request):
    return render(request, 'mindclubapp/index.html')
