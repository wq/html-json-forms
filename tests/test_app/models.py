from django.db import models


class Parent(models.Model):
    name = models.TextField()


class Child(models.Model):
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='children',
    )
    name = models.TextField()
