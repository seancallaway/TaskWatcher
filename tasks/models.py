import datetime
from django.db import models


class Task(models.Model):

    name = models.CharField(max_length=75)
    last_start = models.DateTimeField(null=True, default=None)
    last_finish = models.DateTimeField(null=True, default=None)
    avg_duration = models.DurationField(null=True, default=None)

    def __str__(self):
        return self.name

    def calc_avg_duration(self):
        """
        Calculates the average duration based on TaskHistory.

        Returns average duration as a timedelta or None.
        """
        history_length = self.history.count()
        if history_length > 0:
            durations = self.history.values_list('duration', flat=True)
            avg = sum(durations, datetime.timedelta(0)) / history_length
            return avg
        return None


class TaskHistory(models.Model):

    task = models.ForeignKey(Task, related_name='history', on_delete=models.CASCADE)
    end_time = models.DateTimeField()
    duration = models.DurationField()

    def save(self, *args, **kwargs):
        super(TaskHistory, self).save(*args, **kwargs)
        self.task.avg_duration = self.task.calc_avg_duration()
