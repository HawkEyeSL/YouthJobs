from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import UserRegistrationForm, ApplicantDetailsForm, CompanyDetailsForm
from django.contrib.auth.models import User
from models import Applicants, Companies
from vacancies.models import User_skills
from django.utils import timezone, simplejson
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template import RequestContext
import datetime

def index(request):
  c = {}
  c.update(csrf(request))
  c['form'] = UserRegistrationForm()
  return render_to_response('index.html', c)

def check_username(request): 
  data = {}
  username = request.GET['username'] 
  user = User.objects.get(username=username)
  if user is not None:
    data['msg'] = "Username exists"
  return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def auth_view(request): 
  data = {}
  username = request.GET['username'] 
  password = request.GET['password']  
  user = auth.authenticate(username=username, password=password)
  if user is not None:
    auth.login(request, user)
    request.session['logged_user'] = user.pk
    request.session['logged_username'] = user.username
    data['success'] = True
    data['msg'] = "You have been successfully Logged In"
  else:
    data['success'] = False
    data['msg'] = "There was an error logging you in. Please Try again"
  return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def loggedin(request):
    userObject = User.objects.get(username=request.user.username)
    user_type = userObject.is_staff
    user_foreign_key = userObject.id
    applicantObject = None
    companyObject = None

    print user_type

    if user_type == 0:
      if Applicants.objects.filter(auth_id_id=user_foreign_key).exists():
        applicantObject = Applicants.objects.get(auth_id_id=user_foreign_key)
    else:
      if Companies.objects.filter(auth_id_id=user_foreign_key).exists():
        companyObject = Companies.objects.get(auth_id_id=user_foreign_key)

    if applicantObject is not None or companyObject is not None:
        return HttpResponseRedirect('/wall')
    else:      
      if request.method == 'POST':      
        if user_type == 0:          
          form = ApplicantDetailsForm(request.POST, request.FILES)
          new_applicant = form.save(commit=False)
          new_applicant.auth_id_id = user_foreign_key
          new_applicant.birth_year = request.POST.get('birth_date_year', '')
          new_applicant.birth_month = request.POST.get('birth_date_month', '')
          new_applicant.birth_day = request.POST.get('birth_date_day', '')
          new_applicant.updated = timezone.now()
          new_applicant.created = timezone.now()
          new_applicant.completed = True
          new_applicant.save()
          skills = request.POST.getlist('skills')
          for skill in skills:
            User_skills(user_id_id=new_applicant.pk, skill_id_id=skill.encode('utf8')).save()
        else:
          form = CompanyDetailsForm(request.POST)
          new_company = form.save(commit=False)
          new_company.auth_id_id = user_foreign_key
          new_company.updated = timezone.now()
          new_company.created = timezone.now()
          new_company.completed = True
          new_company.save()
        return HttpResponseRedirect('/wall')

      args = {}
      args.update(csrf(request))

      if user_type == 0:
        args['form'] = ApplicantDetailsForm()
      else:
        args['form'] = CompanyDetailsForm()

      args['username'] = request.user.username
      return render_to_response('loggedin.html', args, context_instance=RequestContext(request))

def invalid_login(request):
  return render_to_response('invalid_login.html')

def logout(request):
  auth.logout(request)
  try:
    request.session['logged_in'] = False
  except KeyError:
    pass
  return HttpResponseRedirect('/')

def register_user(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/register_success')

  args = {}
  args.update(csrf(request))

  args['form'] = UserRegistrationForm()

  return render_to_response('register.html', args)

def register_success(request):
  return render_to_response('register_success.html')

def wall(request):
  if User.objects.get(id=request.session.get('logged_user', False)).is_staff == 0:
    request.session['logged_user_image'] = "images/default.png"
    if Applicants.objects.get(auth_id_id = request.session.get('logged_user', False)) is not None:
      request.session['logged_user_image'] = Applicants.objects.get(auth_id_id = request.session.get('logged_user', False)).thumbnail
    return render_to_response('wall.html', context_instance=RequestContext(request))
  else:
    return render_to_response('company_wall.html', context_instance=RequestContext(request))

def profile(request):
  args = {}
  args['applicant_details'] = applicantObj = Applicants.objects.get(auth_id_id=request.session.get('logged_user', False))
  args['dateOfBirth'] = datetime.date(applicantObj.birth_year, applicantObj.birth_month, applicantObj.birth_day)
  return render_to_response('profile.html', args, context_instance=RequestContext(request))

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
