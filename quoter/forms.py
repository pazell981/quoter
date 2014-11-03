from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	first_name = forms.CharField()
	last_name = forms.CharField()
	password=forms.CharField(max_length=30,widget=forms.PasswordInput())
	password_conf=forms.CharField(max_length=30,widget=forms.PasswordInput())
	email=forms.EmailField(required=False)
	model = User

	def clean_username(self):
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError("this user exist already")


	def clean(self):
		if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password_conf']:
				raise forms.ValidationError("Passwords do not match each other")
			return self.cleaned_data

	def save(self):
		new_user=User.objects.create_user(self.cleaned_data['username'],
		                                  self.cleaned_data['email'],
		                                  self.cleaned_data['password1'])
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.save()