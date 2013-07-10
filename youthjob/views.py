from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import UserRegistrationForm, ApplicantDetailsForm, CompanyDetailsForm
from django.contrib.auth.models import User
from models import Applicants, Companies
from django.utils import timezone

def index(request):
  return render_to_response('index.html')

def login(request):  
  c = {}
  c.update(csrf(request))
  return render_to_response('login.html', c)

def auth_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)

  if user is not None:
    request.session['logged_in'] = True
    auth.login(request, user)
    return HttpResponseRedirect('/loggedin')
  else:
    return HttpResponseRedirect('/invalid')

def loggedin(request):
  if request.session['logged_in'] == True:    
    userObject = User.objects.get(username=request.user.username)
    user_type = userObject.is_staff
    user_foreign_key = userObject.id

    if request.method == 'POST':      
      if user_type == 0:
        form = ApplicantDetailsForm(request.POST)
        new_applicant = form.save(commit=False)
        new_applicant.auth_id_id = user_foreign_key
        new_applicant.birth_year = request.POST.get('birth_date_year', '')
        new_applicant.birth_month = request.POST.get('birth_date_month', '')
        new_applicant.birth_day = request.POST.get('birth_date_day', '')
        new_applicant.updated = timezone.now()
        new_applicant.created = timezone.now()
        new_applicant.completed = True
        new_applicant.save()
      else:
        form = CompanyDetailsForm(request.POST)
        new_company = form.save(commit=False)
        new_company.auth_id_id = user_foreign_key
        new_company.updated = timezone.now()
        new_company.created = timezone.now()
        new_company.save()
      return HttpResponseRedirect('/loggedin')

    args = {}
    args.update(csrf(request))

    if user_type == 0:
      args['form'] = ApplicantDetailsForm()
    else:
      args['form'] = CompanyDetailsForm()

    args['username'] = request.user.username

    return render_to_response('loggedin.html', args)

  else:
    return HttpResponseRedirect('/login')


def invalid_login(request):
  return render_to_response('invalid_login.html')

def logout(request):
  auth.logout(request)
  try:
    request.session['logged_in'] = False
  except KeyError:
    pass
  return HttpResponseRedirect('/login')

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
  return render_to_response('wall.html')