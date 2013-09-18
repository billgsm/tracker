from django.http import HttpResponse


def home(request, name=None):
  if name:
    return HttpResponse('hello %s!' % name)
  else:
    return HttpResponse('hello world!')

