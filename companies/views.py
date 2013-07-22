from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from youthjob.models import Companies, Applicants
from django.template import RequestContext
from vacancies.models import Vacancy, Vacancy_applicants


def list_all(request):
    company_list = Companies.objects.all()
    paginator = Paginator(company_list, 12) # Show 12 contacts per page
    
    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        companies = paginator.page(paginator.num_pages)
    
    return render_to_response('list.html',{'list':companies}, context_instance=RequestContext(request))

def view_applicants(request, vacancy_id):
    args = {}
    applicants_list = Vacancy_applicants.objects.filter(vacancy_id=vacancy_id)
    args['list'] = applicants_list
    paginator = Paginator(applicants_list, 12) # Show 12 contacts per page
    page = request.GET.get('page')
    try:
        vacancies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        vacancies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        vacancies = paginator.page(paginator.num_pages)
    return render_to_response('view_applicants.html', args, context_instance=RequestContext(request))

def view_applicant_details(request, applicant_id):
  args = {}
  applicantObj = Applicants.objects.get(id=applicant_id)
  args['applicant_details'] = applicantObj
  return render_to_response('view_applicant.html', args, context_instance=RequestContext(request))