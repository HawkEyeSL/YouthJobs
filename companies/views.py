from django.shortcuts import render_to_response


from youthjob.models import Companies

def list_all(request):
    return render_to_response('list.html',{'list':Companies.objects.all()})
