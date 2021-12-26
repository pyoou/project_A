from django.db import models


""" class Task docs

    title - title of the task
    content - content about task
    visible - is task want to visible by user
    active - is task allow to be execute
    files - files to task
    user - author of task
    sequence_time - when want to execute task
    replay_at - when want to auto-replay task
    updated_at - last update of task
    created_at - when task has been created

"""


# Task class
class Task(models.Model):
    title = models.CharField(300)
    content = models.CharField(max_length=7000)
    visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    files = models.FileField()
    user = models.ForeignKey()
    sequence_time = models.DateTimeField(auto_now=True, editable=True)
    replay_at = models.DateField(auto_now=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
