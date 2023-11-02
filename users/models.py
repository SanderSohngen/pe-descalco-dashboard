from django.contrib.auth.models import AbstractUser
from django.db import models

from graduation.models import Graduation
from classroom.models import Classroom


class Role(models.TextChoices):
    FOLLOW = 'follow', 'Conduzido'
    LEAD = 'lead', 'Condutor'


class Student(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom, related_name='students')

    def __str__(self):
        return f"{self.role} {self.graduation}"


class Teacher(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        classroom_info = ', '.join([
            f"{classroom.graduation} - {classroom.day}"
            for classroom in self.classrooms.all()
        ])
        return f"{self.role} {classroom_info}"


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    student = models.ManyToManyField(Student, related_name='users')
    teacher = models.ManyToManyField(Teacher, related_name='users', blank=True)
