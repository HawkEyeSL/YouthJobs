from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from youthjob.models import Companies
from django.template import RequestContext
from vacancies.models import Vacancy


def list_all(request):
    companies = []
    company_list = Companies.objects.all()
    for company in company_list:
        companies.append({'name': company.name, 'description': company.description, 'job_posts': Vacancy.objects.get(company_id=company.id).count()})
    paginator = Paginator(companies, 12)  # Show 12 contacts per page

    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        companies = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {'list': companies}, context_instance=RequestContext(request))
