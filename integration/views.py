from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
from rest_framework import generics
from django import forms
from .models import ApprovalRequest
from .serializers import ApprovalRequestSerializer
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
    def get(self, request):
        policy = Policy.objects.first()
        serializer = PolicySerializer(policy)
        return Response(serializer.data)


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
class ApprovalRequestList(APIView):
    def get(self, request):
        approval_requests = ApprovalRequest.objects.all()
        serializer = ApprovalRequestSerializer(approval_requests, many=True)
        return Response(serializer.data)

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