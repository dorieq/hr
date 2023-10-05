from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Department, Location, Position, Employee

class DepartamentAPIView(APIView):
    def post(self, request, format=None):
        rec = request.data.get('departaments', [])
        for dep in rec:
            cur = Department(name=dep)
            cur.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)

class LocationAPIView(APIView):
    def post(self, request, format=None):
        rec = request.data.get('locations', [])
        for dep in rec:
            cur = Location(name=dep)
            cur.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)
    
    
class PositionAPIView(APIView):
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
    def post(self, request, format=None):
        rec = request.data.get('employees', [])
        for dep in rec:
            pos = Position.objects.filter(position=dep["position"]).first()
            emp = Employee(name = dep["name"], iin = dep["iin"], Position = pos)
            emp.save()
        return Response({'message': 'Array received successfully'}, status=status.HTTP_200_OK)
    
