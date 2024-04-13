from django.db import models
from django.contrib.auth.models import User

class Departman(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Personal(models.Model):

    TITLE = (
        ('TD', 'Team Lead'),
        ('MD', 'Mid Lead'),
        ('JR', 'Junior'),
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=10, choices=TITLE, default="Junior")
    gender = models.CharField(max_length=10, choices=GENDER)
    salary = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    departman = models.ForeignKey(Departman, on_delete=models.CASCADE, related_name='personals')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='personals')

    def __str__(self):
        return f"{self.first_name} - {self.title} - {self.departman}"
