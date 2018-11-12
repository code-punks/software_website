from django.shortcuts import render
from rest_framework import viewsets
from homepage.models import *
from .serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(viewsets.ModelViewSet):
	queryset = Profile.objects.all().exclude(rfid__isnull = True)
	serializer_class = ProfileSerializer

class EntryView(viewsets.ModelViewSet):
	queryset = Entry.objects.all()
	serializer_class = EntrySerializer

class ExitView(viewsets.ModelViewSet):
	queryset = Entry.objects.all()
	serializer_class = ExitSerializer

	def put(self, request, pk, format=None):
		device = self.get_object(pk)
		serializer = DeviceSerializer(device, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)