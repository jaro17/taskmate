from django.db import models


class TaskList(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + ' - ' + str(self.done)