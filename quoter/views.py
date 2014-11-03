from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from quoter.forms import UserForm
from django.contrib.auth import authenticate, login
import random

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

def index(request):
	random.shuffle(colors)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'index.html', {"colors": colors})

def register(request):
	random.shuffle(colors)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()
		return render(request, 'register.html', {'user_form': user_form, 'registered': registered, 'colors': colors} )