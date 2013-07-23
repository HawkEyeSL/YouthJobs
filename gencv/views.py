# Create your views here.
from django.shortcuts import render_to_response
from youthjob.models import Applicants
from django.contrib.auth.models import User
from orca.punctuation_settings import cube_root
from vacancies.models import User_skills
from skills.models import Skill
from django.template import RequestContext
import datetime
from models import Applicant_cv
from django.http import HttpResponse
from django.utils import timezone, simplejson

def index(request):
    cv_details = {}
    userObj = Applicants.objects.get(auth_id_id = request.session.get('logged_user', False))
    cv_details['name'] = userObj.full_name
    cv_details['thumbnail'] = userObj.thumbnail
    b_day = "{} / {} / {}".format(userObj.birth_year, userObj.birth_month, userObj.birth_day)
    cv_details['b_day'] = b_day
    cv_details['phone'] = userObj.phone
    cv_details['gender'] = userObj.gender
    cv_details['dateOfBirth'] = datetime.date(userObj.birth_year, userObj.birth_month, userObj.birth_day)
    cv_details['email'] = User.objects.get(id = request.session.get('logged_user', False)).email
    cv_details['address'] = userObj.address
    skillsObjs = User_skills.objects.filter(user_id = userObj.id)
    skills = []
    for skill in skillsObjs:
        skills.append(skill.skill_id)
        
    cv_details['skills'] = skills
    return render_to_response('preview.html', cv_details, context_instance=RequestContext(request))

def view_cv(request):
    args = {}
    applicantObj = Applicants.objects.get(auth_id_id = request.session.get('logged_user', False))
    args['applicant'] = applicantObj
    args['cv'] = Applicant_cv.objects.get(applicant_id_id=applicantObj.id)
    args['dateOfBirth'] = datetime.date(applicantObj.birth_year, applicantObj.birth_month, applicantObj.birth_day)
    args['email'] = User.objects.get(id = request.session.get('logged_user', False)).email
    #print args['cv'].cv
    return render_to_response('view_cv.html', args, context_instance=RequestContext(request))

def save_my_cv(request):
    data = {}
    profile = request.GET['profile'] 
    education = request.GET['education'] 
    experience = request.GET['experience'] 
    projects = request.GET['projects'] 
    applicantObj = Applicants.objects.get(auth_id_id = request.session.get('logged_user', False))
    cv = Applicant_cv(applicant_id=applicantObj, profile=profile, education=education, experience=experience, projects=projects)
    cv.save()
    data['success'] = True
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")