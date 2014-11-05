from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from apps.view_quotes.models import Author, Quote
from django.utils.translation import ugettext, ugettext_lazy as _
import datetime

class UserForm(forms.ModelForm):
	error_messages = {
	  'password_mismatch': _("The two password fields didn't match."),
	}
	password1 = forms.CharField(label=_("Password"),
	  widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
    widget=forms.PasswordInput,
    help_text=_("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name")

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
					code='password_mismatch',
				)
		return password2

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UpdateUser(forms.ModelForm):
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

	def save(self, commit=True):
		self.user.set_password(self.cleaned_data["password2"])
		user = super(UserForm, self).save(commit=False)
		user.password = self.cleaned_data['password1']
		if commit:
			user.save()
		return user

class QuoteForm(forms.Form):
	first_name = forms.CharField(label='Author First Name', max_length=25)
	last_name = forms.CharField(label='Author Last Name', max_length=50)
	quote = forms.CharField(widget=forms.Textarea)
	class Meta:
		fields = ('first_name', 'last_name', 'quote')
	def save(self):
		author = Author.objects.get_or_create(first_name=self.cleaned_data['first_name'],
		                  last_name=self.cleaned_data['last_name'])
		quote = Quote.objects.create(author=author[0], quote=self.cleaned_data['quote'])
		quote.save()
		return quote
			