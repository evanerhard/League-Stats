from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *

def index(request):
	# return HttpResponse('Hello World.')
	context = {
		'title':'Home',
	}
	if request.method == "POST":
		return HttpResponse('Cannot POST here.')
	else:
		return render(request, 'home.html', context)


def register(request):
	if request.method == "POST":
		form = registration_form(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=form.cleaned_data.get('username'),
				password=form.cleaned_data.get('password1'))
			#login call back
			login(request,user)
			return HttpResponseRedirect('/')

	else:
		form = registration_form()
	context = {
		'title':'Register',
		'form':form
	}
	return render(request, 'register.html', context)
