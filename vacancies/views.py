# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import csrf
from forms import JobPostingForm
from django.shortcuts import render_to_response
from youthjob.models import Companies
from vacancies.models import Vacancy, Vacancy_skills, Vacancy_personality
from django.template import RequestContext
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, It works !!!")

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
