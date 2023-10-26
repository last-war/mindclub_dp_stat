from django.forms import ModelForm, CharField, TextInput
from .models import Season, GameType


class GameTypeForm(ModelForm):
    name = CharField(max_length=50, required=True, widget=TextInput())

    class Meta:
        model = GameType
        fields = ['name']


class SeasonForm(ModelForm):
    name = CharField(max_length=50, required=True, widget=TextInput())
    game_type = CharField(max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Season
        fields = ['name']
        exclude = ['game_type']
