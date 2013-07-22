# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import csrf
from forms import JobPostingForm
from django.shortcuts import render_to_response
from youthjob.models import Companies, Applicants
from vacancies.models import Vacancy, Vacancy_skills, Vacancy_personality
from django.template import RequestContext
from django.utils import timezone, simplejson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Vacancy_applicants

def post_job(request):
  success = False
  ctx = None
  logged_user_id = request.session.get('logged_user', False)
  if request.method == 'POST':
    companyObj = Companies.objects.get(auth_id_id=logged_user_id)
    job_form = JobPostingForm(request.POST)
    if job_form.is_valid():
      success = True
      title = job_form.cleaned_data['title']
      description = job_form.cleaned_data['description']
      district = job_form.cleaned_data['district']
      experience = job_form.cleaned_data['experience']
      personality = job_form.cleaned_data['personality']
      vacancy_type = job_form.cleaned_data['vacancy_type']
      salary_ranges = job_form.cleaned_data['salary_ranges']

      new_job = Vacancy(
        company_id=companyObj, 
        name=title, description=description, 
        district=district,
        experience=experience,        
        vacancy_type=vacancy_type,
        salary_ranges=salary_ranges,
        updated=timezone.now(),
        created=timezone.now(),
      )
      new_job.save()

      personality = request.POST.getlist('personality')
      for item in personality:
        Vacancy_personality(vacancy_id_id=new_job.pk, personality_id=item.encode('utf8')).save()

      skills = request.POST.getlist('skills')
      for skill in skills:
        Vacancy_skills(vacancy_id_id=new_job.pk, skill_id_id=skill.encode('utf8')).save()

      new_job_form = JobPostingForm()
      ctx = {'success':success, 'job_form':new_job_form}
    return render_to_response('post_job.html', ctx , context_instance=RequestContext(request))
  else:
    job_form = JobPostingForm()
    ctx = {'job_form':job_form}
    return render_to_response('post_job.html', ctx, context_instance=RequestContext(request))

def vacancies_list(request):
  logged_user_id = request.session.get('logged_user', False)
  companyObj = Companies.objects.get(auth_id_id=logged_user_id)
  vacancy_list = Vacancy.objects.filter(company_id=companyObj.id)
  for vacancy in vacancy_list:
    setattr(vacancy, 'no_of_applicants', Vacancy_applicants.objects.filter(vacancy_id=vacancy.id).count())
  paginator = Paginator(vacancy_list, 12) # Show 12 contacts per page
  page = request.GET.get('page')
  try:
    vacancies = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    vacancies = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    vacancies = paginator.page(paginator.num_pages)
  return render_to_response('vacancies_list.html', {'list':vacancies}, context_instance=RequestContext(request))

def view_vacancy(request, vacancy_id):
  args = {}
  args['applied'] = False
  args['vacancy_id'] = vacancy_id
  args['applicant_id'] = Applicants.objects.get(auth_id_id=request.session.get('logged_user', False)).id
  args['vacancy_details'] = Vacancy.objects.get(id=vacancy_id)  
  if Vacancy_applicants.objects.filter(vacancy_id=vacancy_id, applicant_id=args['applicant_id']).exists():
    args['applied'] = True
  return render_to_response('view_vacancy.html', args, context_instance=RequestContext(request))

def apply(request):
  data = {}
  vacancy_id = request.GET['vacancy_id'] 
  applicant_id = request.GET['applicant_id'] 
  vacancyObj = Vacancy.objects.get(id=vacancy_id)
  applicantObj = Applicants.objects.get(id=applicant_id)
  jobApplication = Vacancy_applicants(vacancy_id=vacancyObj, applicant_id=applicantObj)
  jobApplication.save()
  data['success'] = True
  return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def view_applicants(request, vacancy_id):
    args = {}
    page = request.GET.get('page')
    try:
        vacancies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vacancies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vacancies = paginator.page(paginator.num_pages)
    args['list'] = vacancies
    return render_to_response('view_applicants.html', args, context_instance=RequestContext(request))