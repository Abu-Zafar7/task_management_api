from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    mobile = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Task(models.Model):

    TASK_TYPES = [
        ('PERSONAL', 'Personal'),
        ('WORK', 'Work'),
        ('SHOPPING', 'Shopping'),
        ('OTHER', 'Other'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES, default='OTHER')
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_users = models.ManyToManyField(User, related_name='tasks', blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

