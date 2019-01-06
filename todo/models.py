from django.db import models
from datetime import datetime
class Task_date(models.Model):
    date_added = models.DateField(unique = True)
    objects = models.Manager()
    def __str__(self):
        return str(self.date_added)

class Task_list(models.Model):
    task_date = models.ForeignKey(Task_date,on_delete = models.CASCADE)
    task = models.CharField(max_length = 50)
    due_date = models.DateField()
    is_complete = models.BooleanField(default = False)
    objects = models.Manager()
    def __str__(self):
        return self.task
    



        





