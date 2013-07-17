from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from match.models import Match
from django.template import RequestContext

def list_all(request,vacancy,amount):
    match = Match()
    user_list = match.matchSkills(int(vacancy),int(amount))
    paginator = Paginator(user_list, 12) # Show 12 contacts per page
    
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)
    
    return render_to_response('list.html',{'list':users}, context_instance=RequestContext(request))
