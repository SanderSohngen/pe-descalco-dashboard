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
    result = models.ForeignKey(choices=Result.choices)
    posture = models.ForeignKey(choices=Posture.choices)
    date = models.DateField()
    observations = models.TextField(max_length=500)

    def __str__(self):
        student_name = self.student.users.first().get_full_name()
        student_role = self.student.role
        student_info = f"{student_name} ({student_role})"
        teacher_name = self.teacher.users.first().get_full_name()
        date_str = self.date.strftime('%d/%m/%y')
        return f"{student_info} - {self.result} - {date_str} - {teacher_name}"
