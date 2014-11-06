from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from quoter.forms import UserForm, UpdateUser, QuoteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from apps.view_quotes.models import Quote
import random
import json

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
			user_form.save()
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
	quotes = Quote.objects.select_related().all()
	print dir(quotes)
	if request.method == 'POST':
		quote_form = QuoteForm(data=request.POST)
		if quote_form.is_valid():
			quote = quote_form.save()
			response = {"quote": quote.quote, "first_name": quote.author.first_name, "last_name": quote.author.last_name, "status": "success"}
			quote_form = QuoteForm()
			return HttpResponse(json.dumps(response),
            content_type="application/json"
        		)
			# return render(request, 'quotes.html', {"colors": colors, "quote_form": quote_form, "quotes": quotes})
		else:
			response = {"status": "failure",}
			return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        		)
			# print quote_form.errors
			# return render(request, 'quotes.html', {"colors": colors, "quote_form": quote_form, "quotes": quotes})
	else:
		quote_form = QuoteForm()
		return render(request, 'quotes.html', {"colors": colors, "quote_form": quote_form, "quotes": quotes})

def logout_view(request):
    logout(request)
    return redirect('index')


