from django.shortcuts import render
from getTalent.serializers import UserSerializer, ValidEmailSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from getTalent.models import User

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

class RegisterUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ValidatePrueba(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = ValidEmailSerializer(data=data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)