from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
import random

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

def index(request):
	random.shuffle(colors)
	print colors
	# template = loader.get_template('index.html')
	context = RequestContext(request)
	# return HttpResponse(template.render(context), {"colors": colors})
	return render_to_response('index.html',
	                          {"colors": colors},
	                          context_instance=context)
