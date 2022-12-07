from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
class AddcontactForm(ModelForm):
    class Meta:
        model =  Contact
        fields = '__all__'	
