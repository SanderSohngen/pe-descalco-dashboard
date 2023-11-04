from django.db import models
from classroom.models import Classroom
from graduation.models import Graduation
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()


class Role(models.TextChoices):
    FOLLOW = 'follow', 'Conduzido'
    LEAD = 'lead', 'Condutor'


class Student(models.Model):
    user = models.ForeignKey(
        User, related_name='students', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.LEAD)
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom, related_name='students')

    def __str__(self):
        return f"{self.user.get_full_name()}, {self.role}-{self.graduation}"


class Teacher(models.Model):
    user = models.ForeignKey(
        User, related_name='teachers', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10, choices=Role.choices, default=Role.LEAD)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        classroom_info = ', '.join([
            f"{classroom.graduation} - {classroom.day}"
            for classroom in self.classrooms.all()
        ])
        return f"{self.user.get_full_name()}: {self.role} {classroom_info}"
