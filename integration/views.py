from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import Department, Location, Position, Employee
from drf_yasg import openapi

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
    
