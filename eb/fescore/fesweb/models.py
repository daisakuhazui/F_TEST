from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )
    title = models.CharField(max_length=20)
    content = models.TextField()
