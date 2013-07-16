from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from youthjob.models import Companies
from vacancies.models import Vacancy
from django.template import RequestContext

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

def view_companies(request, company_id):
    args = {}
    args['name'] = Companies.objects.get(id=company_id).name
    vacancy_list = Vacancy.objects.filter(company_id=company_id)
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
    args['list'] = vacancies
    return render_to_response('view_vacancies.html', args, context_instance=RequestContext(request))
