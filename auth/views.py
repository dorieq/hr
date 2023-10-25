from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import PositionSerializer


from .models import UserProfile,Position,Department,Location
from .serializers import UserRegistrationSerializer  # Импортируйте ваш сериализатор

@api_view(['POST'])
def registeruser(request: HttpRequest):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        itin = serializer.validated_data['itin']
        password = serializer.validated_data['password']
        email = serializer.validated_data['email']
        role = serializer.validated_data['role']
        firstname = serializer.validated_data['firstname']
        lastname = serializer.validated_data['lastname']
        phone = serializer.validated_data['phone']
        position = serializer.validated_data['position']

        try:
            user = User.objects.create_user(username=itin, password=password, email=email)
            user_profile = UserProfile(user=user, role=role, phone=phone, position=position)
            user_profile.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

<<<<<<< HEAD
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
=======
@api_view(['POST','GET'])
def custom_login_page(request):
    itin = request.data.get('itin')
    password = request.data.get('password')

    user = authenticate(request, username=itin, password=password)

    if user is not None:
        login(request, user)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, status=status.HTTP_200_OK)
>>>>>>> c78f97ecd1a25229cefa73bd8e605e23f57e3aae
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def loginuser(request):
    if request.method == 'POST':
        itin = request.data.get('itin')
        password = request.data.get('password')

        user = authenticate(request, username=itin, password=password)

        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'GET':
        # Handle the GET request here (e.g., return some information)
        return Response({'message': 'This is a GET request to the login page'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def custom_logout_page(request):
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_by_itin(request, itin):
    try:
        user_profile = UserProfile.objects.get(user__username=itin)
        user_data = {
            'itin': user_profile.user.username,
            'password': user_profile.user.password,
            'email': user_profile.user.email,
            'role': user_profile.role,
            'firstname': user_profile.user.first_name,
            'lastname': user_profile.user.last_name,
            'phone': user_profile.phone,
            'position': user_profile.position,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def get_all_users(request):
    users = UserProfile.objects.all()
    users_list = [{
        'itin': user.user.username,
        'email': user.user.email,
        'role': user.role,
        'firstname': user.user.first_name,
        'lastname': user.user.last_name,
        'phone': user.phone,
        'position': user.position,
    } for user in users]
    return Response(users_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_positions(request):
    positions = Position.objects.all()
    position_list = [{
        'id': position.id,
        'name': position.name,
        # Add other fields as needed
    } for position in positions]
    return Response(position_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_locations(request):
    locations = Location.objects.all()
    location_list = [{
        'id': location.id,
        'name': location.name,
        # Add other fields as needed
    } for location in locations]
    return Response(location_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_departments(request):
    departments = Department.objects.all()
    department_list = [{
        'id': department.id,
        'name': department.name,
        # Add other fields as needed
    } for department in departments]
    return Response(department_list, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_position_by_id(request, position_id):
    try:
        position = Position.objects.get(id=position_id)
        position_data = {
            'id': position.id,
            'name': position.name,
            # Add other fields as needed
        }
        return Response(position_data, status=status.HTTP_200_OK)
    except Position.DoesNotExist:
        return Response({'error': 'Position does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_department_by_id(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
        department_data = {
            'id': department.id,
            'name': department.name,
            # Add other fields as needed
        }
        return Response(department_data, status=status.HTTP_200_OK)
    except Department.DoesNotExist:
        return Response({'error': 'Department does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_location_by_id(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        location_data = {
            'id': location.id,
            'name': location.name,
            # Add other fields as needed
        }
        return Response(location_data, status=status.HTTP_200_OK)
    except Location.DoesNotExist:
        return Response({'error': 'Location does not exist'}, status=status.HTTP_404_NOT_FOUND)