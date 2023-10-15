from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import DepartamentAPIView, LocationAPIView, EmployeeAPIView, PositionAPIView, ExamListView, ExamDetailView, \
    QuestionCreateView, AnswerCreateView, AddMembersView

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('questions/create/', QuestionCreateView.as_view(), name='create-question'),
    path('answers/create/', AnswerCreateView.as_view(), name='create-answer'),
    path('add-exams/', views.AddExamView.as_view()),
    path('add-question/', views.AddQuestionView.as_view()),
    path('add-answers/', views.AddAnswersView.as_view()),
    path('policy/', views.PolicyView.as_view()),
    path('add-application/', views.AddApplicationView.as_view()),
    path('commission/<int:commission_id>/add-members/', AddMembersView.as_view(), name='add-members'),
    path('departaments/', DepartamentAPIView.as_view(), name='departaments'),
    path('locations/', LocationAPIView.as_view(), name='locations'),
    path('employees/', EmployeeAPIView.as_view(), name='employees'),
    path('positions/', PositionAPIView.as_view(), name='positions'),
]
