from django.db import models
from users.models import Student, Teacher
from classroom.models import ClassroomInstance


class Attendance(models.Model):
    classroom_instance = models.ForeignKey(
        ClassroomInstance,
        related_name='%(class)s_attendances',
        on_delete=models.CASCADE
    )
    attended = models.BooleanField(default=False)

    class Meta:
        abstract = True


class StudentAttendance(Attendance):
    student = models.ForeignKey(
        Student, related_name='attendances', on_delete=models.CASCADE)

    def __str__(self):
        attended_str = 'Presente' if self.attended else 'Ausente'
        return f"{self.student} - {self.classroom_instance}, {attended_str}"


class TeacherAttendance(Attendance):
    teacher = models.ForeignKey(
        Teacher, related_name='attendances', on_delete=models.CASCADE)

    def __str__(self):
        attended_str = 'Presente' if self.attended else 'Ausente'
        return f"{self.teacher} - {self.classroom_instance}, {attended_str}"
