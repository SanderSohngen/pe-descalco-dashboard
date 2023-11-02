from math import ceil

from django.db import models
from graduation.models import Criteria
from graduation.models import Graduation


class DayOfWeek(models.TextChoices):
    MONDAY = 'monday', 'Segunda'
    TUESDAY = 'tuesday', 'Terça'
    WEDNESDAY = 'wednesday', 'Quarta'
    THURSDAY = 'thursday', 'Quinta'
    FRIDAY = 'friday', 'Sexta'
    SATURDAY = 'saturday', 'Sábado'
    SUNDAY = 'sunday', 'Domingo'


class Classroom(models.Model):
    start_date = models.DateField()
    day = models.CharField(max_length=10, choices=DayOfWeek.choices)
    time = models.TimeField()
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)

    @property
    def cycle(self):
        month = self.start_date.month
        year = self.start_date.year
        trimester_number = ceil(month/3)
        return f"{trimester_number:02d}/{year}"

    def __str__(self):
        return f"{self.graduation} - {self.day} - {self.cycle}"


class ClassroomInstance(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    criteria = models.ManyToManyField(
        Criteria,
        related_name='classroom_instances',
        blank=True
    )
    subject = models.TextField(max_length=500, blank=True)

    def __str__(self):
        date_str = self.date.strftime('%d/%m/%y')
        return f"{self.classroom.graduation} - {date_str}"