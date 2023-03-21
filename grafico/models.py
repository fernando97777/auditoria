from django.db import models


class Question(models.Model):
    text = models.CharField(
        max_length=255,
        verbose_name='Ingrese la pregunta'
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=10, choices=(('SI', 'SI'), ('NO', 'No')))

    def __str__(self):
        return self.question, self.text
