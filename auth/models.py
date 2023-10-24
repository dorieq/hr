from django.db import models
from django.contrib.auth.models import User
from integration.models import Department,Location,Position


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'auth'

class Employee(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    Position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='auth_employee')

    def __str__(self):
        return self.name

    class Meta:
           app_label = 'auth'
