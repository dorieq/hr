from django.contrib.auth.models import User
from django.db import models

class Policy(models.Model):
    file = models.FileField(upload_to='policies/')

    class Meta:
        verbose_name = 'Политика'
        verbose_name_plural = 'Политика'


class ApplicationStatus(models.Model):

    status = models.CharField(
        max_length=20
    )

    class Meta:
        verbose_name = 'Статус Заявки'
        verbose_name_plural = 'Статус Заявок'

    def __str__(self): 
        return self.status
    
class Location(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

class ExpertCommission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ForeignKey(User, related_name='expert_commissions', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экспертная Комиссия'
        verbose_name_plural = 'Экспертная Комиссия'



class Department(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

class Position(models.Model):

    position = models.CharField(
        max_length=20
    )

    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    Location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

class Employee(models.Model):
    name = models.CharField(max_length=255)
    iin = models.CharField(max_length=12)
    Position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
