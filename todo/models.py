from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

