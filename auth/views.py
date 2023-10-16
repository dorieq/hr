from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@api_view(['POST'])
def register_page(request):
    itin = request.data.get('itin')
    password = request.data.get('password')
    email = request.data.get('email')

    try:
        user = User.objects.create_user(username=itin, password=password, email=email)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def custom_login_page(request):
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
@permission_classes([IsAuthenticated])
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
        user = User.objects.get(username=itin)
        return Response({
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    users_list = [{'username': user.username, 'email': user.email} for user in users]
    return Response(users_list, status=status.HTTP_200_OK)