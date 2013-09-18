from django.http import HttpResponse

from models import Task

def home(request, name=None):
  if name:
    return HttpResponse('hello %s!' % name)
  else:
    return HttpResponse('hello world!')

def ticket_listing(request):
  from django.template import Template, Context
  tickets = Task.objects.all().order_by('-due_date')
  template = Template('{% for elem in objects %} <strong>{{ elem.name }}</strong>: <em>{{ elem.due_date }}</em> <br />{% endfor %}')
  context = Context({'objects': tickets})
  return HttpResponse(template.render(context))
