# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import csrf
from forms import JobPostingForm
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, It works !!!")

def post_job(request):
  print request.POST
  if request.method == 'POST':
    form = JobPostingForm(request.POST)
    new_job = form.save(commit=False)
    new_job.updated = timezone.now()
    new_job.created = timezone.now()
    new_job.save()
    return HttpResponseRedirect('vacancies/postjob')

  args = {}
  args.update(csrf(request))

  args['form'] = JobPostingForm()

  return render_to_response('post_job.html', args)
