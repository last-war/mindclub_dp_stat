from django.db import models


class Command(models.Model):
    name = models.CharField(min_lengt=3, null=False)

    def __str__(self):
        return f'{self.name}'


class Quiz(models.Model):
    date = models.DateField()
    name = models.CharField(min_lengt=3, null=False)

    def __str__(self):
        return f'{self.name} at {self.date}'


class Tour(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE())
    question = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE())
    result = models.FloatField()


class Result(models.Model):
    pass


class Player(models.Model):
    captain = models.BooleanField(default=False)
    pass
