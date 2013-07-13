from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import UserRegistrationForm, ApplicantDetailsForm, CompanyDetailsForm
from django.contrib.auth.models import User
from models import Applicants, Companies
from vacancies.models import User_skills
from django.utils import timezone
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def index(request):
  c = {}
  c.update(csrf(request))
  c['form'] = UserRegistrationForm()
  return render_to_response('index.html', c)

def login(request):  
  c = {}
  c.update(csrf(request))
  return render_to_response('login.html', c)

def auth_view(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)

  if user is not None:
    auth.login(request, user)
    request.session['logged_user'] = user.pk
    return HttpResponseRedirect('/loggedin')
  else:
    return HttpResponseRedirect('/invalid')

def loggedin(request):
    userObject = User.objects.get(username=request.user.username)
    user_type = userObject.is_staff
    user_foreign_key = userObject.id
    applicantObject = None
    companyObject = None

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
      return render_to_response('loggedin.html', args)

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