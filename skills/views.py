from django.utils import simplejson
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from skills.models import Skill
from vacancies.models import User_skills


def search(request,text):
    skills = Skill.objects.filter(name__icontains=text.rstrip('/'))
    skillNames = [y['name'] for y in skills.values()]
    jsondata = simplejson.dumps(skillNames)
    return HttpResponse(jsondata)

def edit(request):
    return render_to_response('editor.html')
    
def add(request):
    return render_to_response('hello.html')

@csrf_exempt
def addUserSkills(request):
    response = request.POST
    newSkills = [ str(x) for x in response.getlist('skills[]')]
    print(newSkills)
    currentUser = request.session.get('logged_user', False)
    Addedskills = [x.skill_id.name for x in User_skills.objects.filter(user_id = currentUser )]
    for newSkill in newSkills:
        if not newSkill in Addedskills:
            User_skills(user_id_id=currentUser, skill_id_id=Skill.objects.get(name = newSkill ).id).save()
    return HttpResponse(simplejson.dumps(str(len(newSkills))+" skills added successfully"), mimetype='application/json')
    
