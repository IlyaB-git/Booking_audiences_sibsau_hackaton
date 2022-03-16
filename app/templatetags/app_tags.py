from atexit import register
from app.forms import *
from django import template
from app.models import *


register = template.Library()

@register.inclusion_tag('app/auditors.html', takes_context=True)
def auditors_tag(context, date=None):
    if date:
        context['auditors'] = Auditor.objects.filter(date=date)
        # broned = Bron.objects.filter(date=date)
        # context['broned'] = broned
    else:
        context['auditors'] = Auditor.objects.all()
    
    context['broned'] = False
    return context

