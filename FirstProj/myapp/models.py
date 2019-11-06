from django.db import models

class Project(models.Model):

    name = models.CharField(max_length=100)

    start_date = models.DateTimeField(auto_now_add=True)

    end_date = models.DateTimeField(auto_now_add=True)


def _str_(self):
    return self.name