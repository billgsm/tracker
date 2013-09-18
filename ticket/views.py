from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Task

def home(request, name=None):
  if name:
    return HttpResponse('hello %s!' % name)
  else:
    return HttpResponse('hello world!')

def ticket_list(request):
  format = '%Y-%m-%d'
  tickets = Task.objects.all()
  if request.method == 'GET':
    if 'closed' in request.GET:
      if request.GET['closed'] == 'true':
        tickets = tickets.filter(closed=True)
      else:
        tickets = tickets.filter(closed=False)
        if 'start' in request.GET and request.GET['start']:
          tickets = tickets.filter(
              due_date__gte=datetime.strptime(request.GET['start'], format))
        if 'end' in request.GET and request.GET['end']:
          tickets = tickets.filter(
              due_date__lte=datetime.strptime(request.GET['end'], format))
  return render_to_response('ticket/list.html', {'objects': tickets})

def ticket_detail(request, id):
  ticket = Task.objects.get(pk=id)
  return render_to_response('ticket/detail.html', {'object': ticket})
