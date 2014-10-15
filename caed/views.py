from django.shortcuts import render
from django.http import HttpResponse
from caed.models import Incident
from django.template import RequestContext, loader

# Create your views here.

def last_incidents(request):
    #if not number:
    #    number = 5
        
    incidents = Incident.objects.all()[:5]
    template = loader.get_template('list_incidents.html')
    context = RequestContext (request, {
        'incidents':incidents,
    })
    
    return HttpResponse(template.render(context))
