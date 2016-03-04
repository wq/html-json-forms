from django.db import models


class Parent(models.Model):
    name = models.TextField()


class Child(models.Model):
    parent = models.ForeignKey(Parent, related_name='children')
    name = models.TextField()
