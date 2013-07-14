from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from skills.models import Skill

def search(request,text):
    skills = Skill.objects.filter(name__contains=text.rstrip('/'))
    skillNames = [y['name'] for y in skills.values()]
    jsondata = simplejson.dumps(skillNames)
    return HttpResponse(jsondata)

def edit(request):
    return render_to_response('editor.html')
    
def add(request):
    return render_to_response('hello.html')

