import datetime
from django.db import models
from django.utils import timezone


class Task(models.Model):

    name = models.CharField(max_length=75)
    last_start = models.DateTimeField(null=True, default=None)
    last_finish = models.DateTimeField(null=True, default=None)
    avg_duration = models.DurationField(null=True, default=None)
    is_running = models.BooleanField(default=False)

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

    def toggle(self):
        now = timezone.now()
        if self.is_running:
            self.is_running = False
            self.last_finish = now
        else:
            self.is_running = True
            self.last_start = now


class TaskHistory(models.Model):

    task = models.ForeignKey(Task, related_name='history', on_delete=models.CASCADE)
    end_time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f'History Item {self.id}'

    def save(self, *args, **kwargs):
        super(TaskHistory, self).save(*args, **kwargs)
        self.task.avg_duration = self.task.calc_avg_duration()
