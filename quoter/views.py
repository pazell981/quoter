from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from quoter.forms import UserForm, UpdateUser, QuoteForm, AuthorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from apps.view_quotes.models import Quote
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
				return HttpResponseRedirect('/quotes')
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
			user.cleanUserData
			user.save()
			registered = True
			return render(request, 'register.html', {'user_form': user_form, 'registered': registered, 'colors': colors} )
		else:
			print user_form.errors
			return render(request, 'register.html', {'user_form': user_form, 'registered': registered, 'colors': colors} )
	else:
		user_form = UserForm()
		return render(request, 'register.html', {'user_form': user_form, 'registered': registered, 'colors': colors} )

@login_required
def update_profile(request):
	random.shuffle(colors)
	if request.method == 'POST':
	  update_form = UpdateUser(data=request.POST, instance=request.user)
	  if form.is_valid():
	  	form.save()
	  	return render(request, 'update_profile.html', {'update_profile': update_form, 'colors': colors})
	  else:
	  	print update_profile.errors
	  	return render(request, 'update_profile.html', {'update_profile': update_form, 'colors': colors})
	else:
	  update_form = UpdateUser(instance=request.user)
	  return render(request, 'update_profile.html', {'update_profile': update_form, 'colors': colors})

@login_required
def quotes(request):
	random.shuffle(colors)
	quotes = Quote.objects.all()
	if request.method == 'POST':
		author_form = AuthorForm(data=request.POST)
		quote_form = QuoteForm(data=request.POST)
		if author_form.is_valid() and quote_form.is_valid():
			author = author_form.save()
			author.save()
			quote = quote_form.save()
			quote.save()
			return render(request, 'quotes.html', {"colors": colors, "author_form": author_form, "quote_form": quote_form})
		else:
			print author_form.errors
			print quote_form.errors
			return render(request, 'quotes.html', {"colors": colors, "author_form": author_form, "quote_form": quote_form})
	else:
		author_form = AuthorForm()
		quote_form = QuoteForm()
		return render(request, 'quotes.html', {"colors": colors, "author_form": author_form, "quote_form": quote_form})

def logout_view(request):
    logout(request)
    return redirect('index')


