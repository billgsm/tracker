from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Task

def home(request, name=None):
  if name:
    return HttpResponse('hello %s!' % name)
  else:
    return HttpResponse('hello world!')

def ticket_listing(request):
  tickets = Task.objects.all().order_by('-due_date')
  return render_to_response('ticket/list.html', {'objects': tickets})
