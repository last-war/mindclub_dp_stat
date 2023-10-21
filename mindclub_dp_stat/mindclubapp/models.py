from django.db import models


# Create your models here.
class GameType(models.Model):
    name = models.CharField(min_lengt=3, null=False)


class Season(models.Model):
    name = models.CharField(min_lengt=3, null=False)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE())


class Quiz(models.Model):
    date = models.DateField()
    name = models.CharField(min_lengt=3, null=False)
    number_tour = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE())
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE())
    description = models.TextField()
    max_command = models.IntegerField()
    total_result = models.FloatField()

    def __str__(self):
        return f'{self.name} at {self.date}'


class Player(models.Model):
    captain = models.BooleanField(default=False)
    name = models.CharField(min_lengt=3, null=False)
    phone = models.CharField(min_lengt=3, null=False)


class Command(models.Model):
    name = models.CharField(min_lengt=3, null=False)
    cap = models.ForeignKey(Player, on_delete=models.CASCADE())
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE())


class Tour(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE())
    number_question = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE())
    result = models.FloatField()


class Question(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE())
    text_question = models.TextField()
    text_answer = models.TextField()
    point = models.FloatField()
    is_multi_question = models.BooleanField()
    is_media_content = models.BooleanField()
    parent_question = models.ForeignKey(Question)


class MultiContent(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE())
    media_content = models.BinaryField()


class Result(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE())
    result = models.FloatField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE())

    def __str__(self):
        return f'{self.name}'


