from django.db import models
from django.db.models import ManyToManyField


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deadline_time = models.DateTimeField(
        auto_now_add=False,
        null=True,
        blank=True,
    )
    is_done = models.BooleanField(default=False)
    tags = ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("is_done", "-created_time",)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
