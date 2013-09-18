from datetime import timedelta, date

from django.template.defaultfilters import date as django_date
from django.db import models

class Task(models.Model):
  name = models.CharField(max_length=250)
  description = models.TextField()
  created_date = models.DateField(auto_now_add=True)
  due_date = models.DateField()
  schedule_date = models.DateField()
  closed = models.BooleanField(default=False)

  def __unicode__(self):
    return u'{0}'.format(self.name)

  def colored_due_date(self):
    # Internationalization is still available when converting like that
    due_date = django_date(self.due_date, "d F Y")
    if self.due_date - timedelta(days=7) > date.today():
      color = 'green'
    elif self.due_date - timedelta(days=7) < date.today() and \
        self.due_date >= date.today():
      color = 'orange'
    else:
      color = 'red'

    return u'<span style="color: {0};">{1}</span>'.format(color, due_date)

  # Allow html tags, do not escape them for this function
  colored_due_date.allow_tags = True


  def remaining_days(self):
    r_days = int(self.due_date.strftime("%d")) - int(date.today().strftime("%d"))
    if r_days >= 0:
      return u'{0} day(s) left.'.format(r_days)
    return u'Due date exceeded by {0} day(s).'.format(-r_days)

