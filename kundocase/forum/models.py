from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
