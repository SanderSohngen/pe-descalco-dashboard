from django.db import models


class Graduation(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Criteria(models.Model):
    graduation = models.ForeignKey(
        Graduation,
        related_name="criterias",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name
