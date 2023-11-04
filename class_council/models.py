from django.db import models
from users.models import Student, Teacher


class Posture(models.TextChoices):
    PERFECT = 'perfect', 'Perfeito'
    GOOD = 'good', 'Bom'
    AVERAGE = 'average', 'Médio'
    POOR = 'poor', 'Ruim'
    AWFUL = 'awful', 'Péssimo'


class Result(models.TextChoices):
    APPROVED = 'approved', 'Aprovado'
    FAILED = 'failed', 'Reprovado'


class ClassCouncil(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    result = models.CharField(
        max_length=10, choices=Result.choices, default=Result.FAILED)
    posture = models.CharField(
        max_length=10, choices=Posture.choices, default=Posture.FAILED)
    date = models.DateField()
    observations = models.TextField(max_length=500)

    def __str__(self):
        teacher_name = self.teacher.user.get_full_name()
        date_str = self.date.strftime('%d/%m/%y')
        return f"{self.student} - {self.result} - {date_str} - {teacher_name}"
