from django.db import models
from users.models import NewUser
from django.utils.translation import gettext_lazy as _


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


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'


class TaskFile(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.RESTRICT, to_field='id')
    path = models.FileField(upload_to=user_directory_path)


# Task model to database
class Task(models.Model):
    title = models.CharField(_("title"), max_length=300)
    content = models.CharField(_("content"), max_length=7000)
    visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(NewUser, on_delete=models.RESTRICT, to_field='id')
    sequence_time = models.DateTimeField(auto_now=True, editable=True)
    replay_at = models.DateField(auto_now=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.user}: {self.title}"
