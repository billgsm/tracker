from django.contrib import databrowse

from models import Task

databrowse.site.register(Task)
