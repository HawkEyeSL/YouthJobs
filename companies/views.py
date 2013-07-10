from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from youthjob.models import Companies

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
    
    return render_to_response('list.html',{'list':companies})
