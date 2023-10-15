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
class Application(models.Model):
    current_location = models.CharField(max_length=255, default='Default Location')
    # поля!!!!!.
    status = models.ForeignKey(ApplicationStatus, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class ApplicationTemplate(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ARCHIVED', 'Archived'),
    ]
    name = models.CharField(max_length=255)
    template = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE',
    )

    class Meta:
        verbose_name = 'Шаблон Заявки'
        verbose_name_plural = 'Шаблон Заявок'

    def __str__(self):
        return self.name

    
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
class StatisticData(models.Model):
    label = models.CharField(max_length=255, verbose_name='Метка')
    value = models.IntegerField(verbose_name='Значение')

    class Meta:
        verbose_name = 'Данные статистики'
        verbose_name_plural = 'Данные статистики'

    def __str__(self):
        return self.label
class Employee(models.Model):
    name = models.CharField(max_length=255)
    iin = models.CharField(max_length=12)
    Position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class Exam(models.Model):
    title = models.TextField()
    instruction = models.TextField()
    duration = models.IntegerField()
    access = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'
    def __str__(self):
        return self.title


class Question(models.Model):
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()
    answerPosition: models.IntegerField
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answers(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionPosition = models.IntegerField()
    option: models.TextField()


    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
class ApprovalRequest(models.Model):
    status_choices = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, null=True, blank=True, choices=status_choices)
    iin = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"ApprovalRequest {self.id}"

class Resume(models.Model):
    iin = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='resumes_as_iin')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='resumes_as_name')
    pdf_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name