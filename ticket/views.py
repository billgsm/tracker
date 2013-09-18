from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Task

def home(request, name=None):
  if name:
    return HttpResponse('hello %s!' % name)
  else:
    return HttpResponse('hello world!')

def ticket_list(request, filter):
  if filter == 'closed':
    tickets = Task.objects.filter(closed=True)
  elif filter == 'opened':
    tickets = Task.objects.filter(closed=False)
  elif filter == 'week':
    tickets = Task.objects.filter(
        due_date__lte=date.today() + timedelta(days=7),
        due_date__gte=date.today())
  elif filter == 'all':
    tickets = Task.objects.all().order_by('-due_date')
  return render_to_response('ticket/list.html', {'objects': tickets})

def ticket_detail(request, id):
  ticket = Task.objects.get(pk=id)
  return render_to_response('ticket/detail.html', {'object': ticket})
