from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework import generics
from homepage.models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpRequest
import requests
import json
from datetime import datetime
User = get_user_model()

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class ProfileView(viewsets.ModelViewSet):
	queryset = Profile.objects.all().exclude(rfid__isnull = True)
	serializer_class = ProfileSerializer
	filter_fields = ('rfid',)
	filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
	permission_classes = (permissions.IsAdminUser)

class EntryView(viewsets.ModelViewSet):
	queryset = Entry.objects.all()
	serializer_class = EntrySerializer


class ExitView(viewsets.ModelViewSet):
	queryset = Entry.objects.all()
	serializer_class = ExitSerializer

	# def put(self, request, pk, format=None):
	# 	device = self.get_object(pk)
	# 	print(device)
	# 	serializer = DeviceSerializer(device, data=request.data)
	# 	if serializer.is_valid():
	# 		user_link = serializer.data['user']
	# 		print(user_link)
	# 		req = requests.get(user_link)
	# 		response = json.loads(req.content)
	# 		user = response['user']
	# 		print(user)
	# 		bill_objects = Bill.objects.all().filter(rfid__username__exact = user)
	# 		entry_objects = Entry.objects.all().filter(rfid__username__exact = user)
	# 		l = []
	# 		if entry_objects != None:
	# 			for obj in entry_objects:
	# 				if obj.month == datetime.now().month:
	# 					l.append(obj)
	# 		amount_ = 0
	# 		for obj in l:
	# 			amount_ += obj.amount

	# 		if bill_objects == None :
	# 			bill_object = Bill(rfid=user,month=datetime.now().month,monthly_amount=amount)
	# 			bill_object.save()
	# 		else:
	# 			bl = []
	# 			for obj in bill_object:
	# 				if obj.month == datetime.now().month:
	# 					bl.append(obj)
	# 			for obj in bl:
	# 				obj.amount = amount_
	# 				obj.save()
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
	def update(self,request, *args, **kwargs):
		entries = self.get_object()
		print(entries)
		serializer = self.serializer_class(entries,data=request.data,context={'request': request})
		print(request.data)
		if serializer.is_valid():
			user= serializer.validated_data['user']
			# req = requests.get(user_link)
			# response = json.loads(req.content)
			# user = response['user']
			print(user)
			bill_objects = Bill.objects.all().filter(rfid__username__exact = user)
			entry_objects = Entry.objects.all().filter(user__exact = user)
			l = []
			if entry_objects != None:
				for obj in entry_objects:
					if int(obj.exit_time.strftime("%m")) == datetime.now().month:
						l.append(obj)
			print(len(l))
			print(bill_objects)
			amount_ = 0
			for obj in l:
				amount_ += obj.amount
				print(obj.amount)

			if len(bill_objects) == 0 :
				bill_object = Bill.objects.create(rfid=user,month=datetime.now().month,monthly_amount=amount_)
				# bill_object.save()
			else:
				bl = []
				for obj in bill_objects:
					if obj.month == datetime.now().month:
						bl.append(obj)
				for obj in bl:
					obj.amount = amount_
					obj.save()
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
