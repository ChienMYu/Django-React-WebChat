from django.db import models

#import user
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} | {self.content[:10]}...'

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]

