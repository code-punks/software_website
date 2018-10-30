from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
from .models import *
from django.forms.extras import SelectDateWidget
from datetimepicker.widgets import DateTimePicker
from django.contrib.admin.widgets import AdminDateWidget

User = get_user_model()


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password did not match"
            )


class EditProfileForm2(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('location','birthdate','bio','phone_number',)	

	location = forms.CharField(max_length=30, required=True,label = 'Location')
	birthdate = forms.DateField(required=True, label = 'Date of Birth', widget=SelectDateWidget(years = range(1900,2000)))
	bio = forms.CharField(widget=forms.Textarea,max_length=500, required=False, label = 'Bio' )
	phone_number = forms.IntegerField(required=True, label = 'Phone Number (After +91)')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
