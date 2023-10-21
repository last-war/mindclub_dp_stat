from django.contrib import admin
from .models import GameType, Season, Quiz, Player, Command, Tour, Question, Subquestion, MultiContent, Result

# Register your models here.
admin.site.register(GameType)
admin.site.register(Season)
admin.site.register(Quiz)
admin.site.register(Player)
admin.site.register(Command)
admin.site.register(Tour)
admin.site.register(Question)
admin.site.register(Subquestion)
admin.site.register(MultiContent)
admin.site.register(Result)
