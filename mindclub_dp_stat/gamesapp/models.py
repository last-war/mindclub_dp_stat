from django.db import models


class Command(models.Model):
    name = models.CharField(min_lengt=3, null=False)
# quiz_id?

    def __str__(self):
        return f'{self.name}'


class Quiz(models.Model):
    date = models.DateField()
    name = models.CharField(min_lengt=3, null=False)
    number_tour = models.IntegerField()
    #number_command?

    def __str__(self):
        return f'{self.name} at {self.date}'


class Tour(models.Model):
    number_question = models.IntegerField()
    total_result = models.FloatField()
    question = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE())


class Result(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE())
    point = models.FloatField()
    question_number = models.IntegerField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE())


class Player(models.Model):
    captain = models.BooleanField(default=False)
    pass
