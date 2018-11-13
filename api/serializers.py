from rest_framework import serializers
from homepage.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profile
		fields = ('url', 'user', 'rfid')

class EntrySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Entry
		fields = ('id','url','user','entry_time','exit_time','time','amount')

class ExitSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Entry
		fields = ('id','url','user','exit_time')