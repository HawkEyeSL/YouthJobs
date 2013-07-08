from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import UserRegistrationForm

def index(request):
  return render_to_response('index.html')

def login(request):  
  c = {}
  c.update(csrf(request))
  return render_to_response('login.html', c)

def auth_view(request):
  print(request)
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)

  if user is not None:
    request.session['logged_in'] = True
    auth.login(request, user)
    return HttpResponseRedirect('/loggedin')
  else:
    return HttpResponseRedirect('/invalid')

def loggedin(request):
  if request.session['logged_in'] == True:
    return render_to_response('loggedin.html', {'full_name' : request.user.username})
  else:
    return HttpResponseRedirect('/login')


def invalid_login(request):
  return render_to_response('invalid_login.html')

def logout(request):
  auth.logout(request)
  try:
    request.session['logged_in'] = False
  except KeyError:
    pass
  return HttpResponseRedirect('/login')

def register_user(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/register_success')

  args = {}
  args.update(csrf(request))

  args['form'] = UserRegistrationForm()

  return render_to_response('register.html', args)

def register_success(request):
  return render_to_response('register_success.html')