from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers

from .models import *
from .forms import *

import json
import nfldb

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

@csrf_exempt
def players_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		players = serializers.serialize('json',Player.objects.all())
		return HttpResponse(players, content_type="application/json")

@csrf_exempt
def five_qb_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		players = serializers.serialize('json',Player.objects.all())
		qbs = {}
		qbs['Player']=[]
		db = nfldb.connect()
		q = nfldb.Query(db)
		q.game(season_year=2015, season_type='Regular')
		for g in q.sort('passing_yds').limit(5).as_aggregate():
			qbs['Player'] +=[{
				'id':g.player,
				'yds':g.passing_yds,

			}]
		# return JsonResponse(qbs)
		return HttpResponse(qbs, content_type="application/json")

	else:
		return HttpResponse("404")
		# return render(request, 'top.html',context)
