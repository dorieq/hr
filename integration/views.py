from io import BytesIO

from django.contrib.sites import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
from rest_framework import generics
from django import forms
from .models import ApprovalRequest, Resume
from .serializers import ApprovalRequestSerializer, ResumeSerializer
from .serializers import ExamSerializer, AnswersSerializer, QuestionSerializer, DepartmentSerializer, \
    EmployeeSerializer, PolicySerializer, ApplicationSerializer, LocationSerializer
from .models import Policy, ExpertCommission
from django.views.generic.edit import FormView
from .forms import AddMembersForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Department, Location, Position, Employee

class DepartamentAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('departaments', openapi.IN_QUERY, description="Массив департаментов", type=openapi.TYPE_ARRAY, items=openapi.Items(type="string")),
        ],
        responses={200: 'Array received successfully', 400: 'Bad Request'},
    )

    def post(self, request, format=None):
        rec = request.data.get('departaments', [])
        for dep in rec:
            cur = Department(name=dep)
            cur.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)

class LocationAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('locations', openapi.IN_QUERY, description="Массив локации", type=openapi.TYPE_ARRAY, items=openapi.Items(type="string")),
        ],
        responses={200: 'Array received successfully', 400: 'Bad Request'},
    )
    def post(self, request, format=None):
        rec = request.data.get('locations', [])
        for dep in rec:
            cur = Location(name=dep)
            cur.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)
    
    
class PositionAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('positions', openapi.IN_QUERY, description="Массив должностей", type=openapi.TYPE_ARRAY, items=openapi.Items(type="string")),
        ],
        responses={200: 'Array received successfully', 400: 'Bad Request'},
    )
    def post(self, request, format=None):
        rec = request.data.get('positions', [])
        print(rec)
        for cur in rec:
            loc = Location.objects.filter(name=cur["location"]).first()
            dep = Department.objects.filter(name=cur["department"]).first()
            pos = Position(position=cur["name"], Department=dep, Location=loc)
            pos.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)
    

class EmployeeAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('employees', openapi.IN_QUERY, description="Массив работников", type=openapi.TYPE_ARRAY, items=openapi.Items(type="string")),
        ],
        responses={200: 'Array received successfully', 400: 'Bad Request'},
    )
    def post(self, request, format=None):
        rec = request.data.get('employees', [])
        for dep in rec:
            pos = Position.objects.filter(position=dep["position"]).first()
            emp = Employee(name = dep["name"], iin = dep["iin"], Position = pos)
            emp.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)
    
@permission_classes([IsAuthenticated])
class ExamListView(APIView):
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            exam = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
class ExamDetailView(APIView):
    def get(self, request, pk):
        exam = Exam.objects.get(pk=pk)
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    def put(self, request, pk):
        exam = Exam.objects.get(pk=pk)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exam = Exam.objects.get(pk=pk)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@permission_classes([IsAuthenticated])
class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AddExamView(APIView):
    def post(self, request):
        serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            exam = serializer.save()
            return Response(
                {"isSuccessful": True, "message": "Exam saved successfully", "exam": ExamSerializer(exam).data})
        else:
            return Response({"isSuccessful": False, "message": "Action Failed. Exam could not be saved",
                             "errors": serializer.errors})


class AddQuestionView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            question = serializer.save()
            return Response({"isSuccessful": True, "message": "Question saved successfully",
                             "question": QuestionSerializer(question).data})
        else:
            return Response({"isSuccessful": False, "message": "Action Failed. Question could not be saved",
                             "errors": serializer.errors})


class AddAnswersView(APIView):
    def post(self, request):
        serializer = AnswersSerializer(data=request.data)

        if serializer.is_valid():
            answer = serializer.save()
            return Response({"isSuccessful": True, "message": "Answer saved successfully",
                             "answer": AnswersSerializer(answer).data})
        else:
            return Response({"isSuccessful": False, "message": "Action Failed. Answer could not be saved",
                             "errors": serializer.errors})


class AddApplicationView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)

        if serializer.is_valid():
            application = serializer.save()
            return Response({"isSuccessful": True, "message": "Application saved successfully",
                             "application": ApplicationSerializer(application).data})
        else:
            return Response({"isSuccessful": False, "message": "Action Failed. Application could not be saved",
                             "errors": serializer.errors})

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

class PolicyView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('file', openapi.IN_QUERY, description="Policy File",
                              type=openapi.TYPE_STRING),
        ],
        responses={200: 'Policy data received successfully', 400: 'Bad Request'},
    )
    def get(self, request):
        policy = Policy.objects.first()
        serializer = PolicySerializer(policy)
        return Response(serializer.data)


    def post(self, request):
        pdf_url = request.data.get("file")  # Предположим, что ссылка на PDF находится в поле "pdf_url" запроса

        if not pdf_url:
            return Response({"isSuccessful": False, "message": "PDF URL is missing"})

        # Загружаем PDF файл по ссылке
        response = requests.get(pdf_url)

        if response.status_code == 200:
            # Создаем InMemoryUploadedFile из байтового содержимого PDF
            pdf_file = BytesIO(response.content)
            pdf_file.name = "policy.pdf"  # Задайте имя файла, как вам нужно

            data = request.data.copy()
            data["file"] = pdf_file  # Замените "pdf_field_name" на имя поля в вашей сериализаторе

            serializer = PolicySerializer(data=data)

            if serializer.is_valid():
                policy = serializer.save()
                return Response({"isSuccessful": True, "message": "Policy saved successfully",
                                 "answer": AnswersSerializer(policy).data})
            else:
                return Response({"isSuccessful": False, "message": "Action Failed. Policy could not be saved",
                                 "errors": serializer.errors})
        else:
            return Response({"isSuccessful": False, "message": "Failed to download PDF from the provided URL"})



class ExpertCommissionForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select'}),
    )

    class Meta:
        model = ExpertCommission
        fields = ['name', 'members']


class AddMembersView(FormView, APIView):
    template_name = 'add_members.html'
    form_class = AddMembersForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commission_id'] = self.kwargs['commission_id']
        return context

    def form_valid(self, form):
        commission_id = self.kwargs['commission_id']
        commission = ExpertCommission.objects.get(pk=commission_id)
        members = form.cleaned_data['members']
        commission.members.add(*members)
        return super().form_valid(form)
class AllUserApprovalRequest(APIView):


    def get(self, request):
        approval_requests = ApprovalRequest.objects.all()
        serializer = ApprovalRequestSerializer(approval_requests, many=True)
        return Response(serializer.data)

    status_choices = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="ID",
                              type=openapi.TYPE_ARRAY, items=openapi.Items(type="integer")),
            openapi.Parameter('status', openapi.IN_QUERY, description="Status",
                              type=openapi.TYPE_STRING, enum=list(status_choices)),
            openapi.Parameter('iin', openapi.IN_QUERY, description="Employee's ID",
                              type=openapi.TYPE_INTEGER),
        ],
        responses={200: 'Data received successfully', 400: 'Bad Request'},
    )
    def post(self, request):
        serializer = ApprovalRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApprovalRequestDetail(APIView):
    def get(self, request, pk):
        try:
            approval_request = ApprovalRequest.objects.get(pk=pk)
        except ApprovalRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ApprovalRequestSerializer(approval_request)
        return Response(serializer.data)

    status_choices = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="ID",
                              type=openapi.TYPE_ARRAY, items=openapi.Items(type="integer")),
            openapi.Parameter('status', openapi.IN_QUERY, description="Status",
                              type=openapi.TYPE_STRING, enum=list(status_choices)),
            openapi.Parameter('iin', openapi.IN_QUERY, description="Employee's ID",
                              type=openapi.TYPE_INTEGER),
        ],
        responses={200: 'Data received successfully', 400: 'Bad Request'},
    )
    def put(self, request, pk):
        try:
            approval_request = ApprovalRequest.objects.get(pk=pk)
        except ApprovalRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ApprovalRequestSerializer(approval_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            approval_request = ApprovalRequest.objects.get(pk=pk)
        except ApprovalRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        approval_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResumeList(APIView):
    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Name", type=openapi.TYPE_STRING),
            openapi.Parameter('iin', openapi.IN_QUERY, description="Employee's ID", type=openapi.TYPE_STRING),
            openapi.Parameter('department', openapi.IN_QUERY, description="Department", type=openapi.TYPE_STRING),
            openapi.Parameter('location', openapi.IN_QUERY, description="Location", type=openapi.TYPE_STRING),
        ],
        responses={200: 'Data received successfully', 400: 'Bad Request'},
    )
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResumeDetail(APIView):
    def get(self, request, pk):
        try:
            resume = Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ResumeSerializer(resume)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="Name", type=openapi.TYPE_STRING),
            openapi.Parameter('iin', openapi.IN_QUERY, description="Employee's ID", type=openapi.TYPE_STRING),
            openapi.Parameter('department', openapi.IN_QUERY, description="Department", type=openapi.TYPE_STRING),
            openapi.Parameter('location', openapi.IN_QUERY, description="Location", type=openapi.TYPE_STRING),
        ],
        responses={200: 'Data received successfully', 400: 'Bad Request'},
    )
    def put(self, request, pk):
        try:
            resume = Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ResumeSerializer(resume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            resume = Resume.objects.get(pk=pk)
        except Resume.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        resume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ResumePDF(APIView):
    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        pdf_file = resume.pdf_file
        if pdf_file:
            response = FileResponse(pdf_file.open(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf_file.name}"'
            return response
        else:
            return Response("PDF file not found", status=status.HTTP_404_NOT_FOUND)