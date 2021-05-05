from django import forms 
from django.contrib.auth.models import User

class SigninWithEmailForm(forms.Form):
	class Meta:
		model = User
		fields = ['email',]
	
class RegisterUserForm(forms.Form):
	# class Meta: 
	# 	model = User
	# 	fields = ['username', 'email', 'password',]
	username = forms.CharField(max_length = 200)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput) 
	password_rpt = forms.CharField(max_length=32, widget=forms.PasswordInput) 
	email = forms.CharField(max_length = 200)
