from django.db import models


class Day(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime('%d/%m/%y')
