from rest_framework import serializers
from .models import Exam, Question, Answers, Department, Employee, Policy, Application, Location, ApprovalRequest, \
    Resume


class ExamSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    instruction = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()
    access = serializers.BooleanField()

    class Meta:
        model = Exam
        fields = ['title', 'instruction', 'duration', 'access']

    def get_title(self, obj):
        return obj.title

    def get_instruction(self, obj):
        return obj.instruction

    def get_duration(self, obj):
        return obj.duration

    def get_access(self, obj):
        return obj.access


class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=255)
    examId = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    answerPosition = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ['question', 'examId', 'answerPosition']

    def get_question(self, obj):
        return obj.question

    def get_examId(self, obj):
        return obj.examId

    def get_answerPosition(self, obj):
        return obj.answerPosition


class AnswersSerializer(serializers.ModelSerializer):
    questionId = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    questionPosition = serializers.IntegerField()
    option = serializers.CharField(max_length=255)

    class Meta:
        model = Answers
        fields = ['questionId', 'questionPosition', 'option']

    def get_questionId(self, obj):
        return obj.questionId

    def get_questionPosition(self, obj):
        return obj.questionPosition

    def get_option(self, obj):
        return obj.option

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = ['name', 'department']
    
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['file']

class ApplicationSerializer(serializers.ModelSerializer):
    current_location = serializers.CharField(max_length=255)

    class Meta:
        model = Application
        fields = ['status', 'current_location'] 

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name']
class ApprovalRequestSerializer(serializers.ModelSerializer):
    iin = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    class Meta:
        model = ApprovalRequest
        fields = '__all__'
        extra_kwargs = {
            'iin': {'required': False}
        }


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'