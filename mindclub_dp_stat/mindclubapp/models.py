from django.db import models


# Create your models here.
class GameType(models.Model):
    name = models.CharField(null=False)


class Season(models.Model):
    name = models.CharField(null=False)
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.gametype} з {self.name}'


class Quiz(models.Model):
    date = models.DateField()
    name = models.CharField(null=False)
    number_tour = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE)
    description = models.TextField()
    max_command = models.IntegerField()
    total_result = models.FloatField()

    def __str__(self):
        return f'{self.name} at {self.date}'


class Player(models.Model):
    captain = models.BooleanField(default=False)
    name = models.CharField(null=False)
    phone = models.CharField(null=False)


class Command(models.Model):
    name = models.CharField(null=False)
    cap = models.ForeignKey(Player, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class Tour(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    number_question = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    result = models.FloatField()


class Question(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    text_question = models.TextField()
    text_answer = models.TextField()
    point = models.FloatField()
    is_multi_question = models.BooleanField()
    is_media_content = models.BooleanField()


class Subquestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_question = models.TextField()
    text_answer = models.TextField()
    point = models.FloatField()
    is_media_content = models.BooleanField()


class MultiContent(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subquestion = models.ForeignKey(Subquestion, on_delete=models.CASCADE)
    media_content = models.BinaryField()


class Result(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    result = models.FloatField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
