from django.forms import ModelForm, CharField, TextInput
from .models import Season, GameType


class GameTypeForm(ModelForm):
    name = CharField(min_length=0, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = GameType
        fields = ['name']


class SeasonForm(ModelForm):
    name = CharField(min_length=0, max_length=50, required=True, widget=TextInput())
    game_type = CharField(min_length=0, max_length=50, widget=TextInput())

    class Meta:
        model = Season
        fields = ['name', 'game_type']
