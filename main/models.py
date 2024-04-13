from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)
    asked_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    votes = models.ManyToManyField(User, related_name="questions_liked", blank=True)

    def get_absolute_url(self):
        return reverse("question", kwargs={"id": self.id})


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    answered_by = models.ForeignKey(User, related_name="answers", on_delete=models.CASCADE)
    answered_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='answer_images/', blank=True, null=True) # New field for image
    votes = models.ManyToManyField(User, related_name="answers_liked", blank=True)
