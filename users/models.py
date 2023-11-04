from django.db import models
from classroom.models import Classroom
from graduation.models import Graduation
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        return self.email


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
