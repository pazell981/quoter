from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	first_name = forms.CharField()
	last_name = forms.CharField()
	password1=forms.CharField(label='Password',max_length=30,widget=forms.PasswordInput())
	password2=forms.CharField(label='Password Confirmation',max_length=30,widget=forms.PasswordInput())
	email=forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "password1", "password2")

	def cleanUserData(self):
		super(UserForm, self).clean()
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if not password2:
			raise forms.ValidationError("You must confirm your password")
		if password1 != password2:
			raise forms.ValidationError("Your passwords do not match")
		return password2

	def save(self):
		self.user.set_password(self.cleaned_data["password2"])
		new_user=User.objects.create_user(self.cleaned_data['username'],
		                                  self.cleaned_data['email'],
		                                  self.cleaned_data['password1'])
		new_user.first_name = self.cleaned_data['first_name']
		new_user.last_name = self.cleaned_data['last_name']
		new_user.save()