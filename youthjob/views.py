from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, AITI-2013. You're at the simplecal.")

