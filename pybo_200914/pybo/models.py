from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content
