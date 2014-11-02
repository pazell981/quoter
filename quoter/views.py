from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader

def index(request):
  template = loader.get_template('index.html')
  context = RequestContext(request)
  return HttpResponse(template.render(context))