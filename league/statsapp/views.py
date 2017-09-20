from django.shortcuts import render,HttpResponse, HttpResponseRedirect, get_object_or_404
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

@csrf_exempt
def drives_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		drives = serializers.serialize('json',Drive.objects.all()[:10])
		json_drives = json.loads(drives)
		# return HttpResponse(games, content_type="application/json")
		return render(request, 'drives.html', {'drives_list':json_drives})

def drive_view(request, drive_id):
	drve = Drive.objects.get(drive_id=drive_id)
	context = {
		'gsis_id':drve.gsis,
		'drive_id':drve.drive_id,
		'start_time':drve.start_time,
		'start_field':drve.start_field,
		'end_field':drve.end_field,
		'end_time':drve.end_time,
		'pos_team':drve.pos_team,
		'pos_time':drve.pos_time,
		'first_downs':drve.first_downs,
		'result':drve.result,
		'penalty_yards':drve.penalty_yards,
		'yards_gained':drve.yards_gained,
		'play_count':drve.play_count,
		'time_inserted':drve.time_inserted,
		'time_updated':drve.time_updated,

	}
	return render(request, "drive_view.html", context)

@csrf_exempt
def games_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		games = serializers.serialize('json',Game.objects.all()[:10])
		json_games = json.loads(games)
		# return HttpResponse(games, content_type="application/json")
		return render(request, 'games.html', {'games_list':json_games})

def game_view(request, gsis_id):
	gme = Game.objects.get(gsis_id=gsis_id)
	context = {
		'gsis_id':gme.gsis_id,
		'gamekey':gme.gamekey,
		'start_time':gme.start_time,
		'week':gme.week,
		'day_of_week':gme.day_of_week,
		'season_year':gme.season_year,
		'season_type':gme.season_type,
		'finished':gme.finished,
		'home_team':gme.home_team,
		'home_score':gme.home_score,
		'home_turnovers':gme.home_turnovers,
		'away_team':gme.away_team,
		'away_score':gme.away_score,
		'away_turnovers':gme.away_turnovers,
		'time_inserted':gme.time_inserted,
		'time_updated':gme.time_updated,

	}
	return render(request, "game_view.html", context)


@csrf_exempt
def play_list(request):

	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		plays = serializers.serialize('json',Play.objects.all()[:10])
		json_plays = json.loads(plays)
		# return HttpResponse( players, content_type='application/json')
		return render(request, 'plays.html', {'plays_list':json_plays})

# def play_view(request, play_id):
# 	ply = Play.objects.get(play_id=play_id)
# 	context = {
# 		'gsis':ply.gsis,
# 		'play_id':ply.play_id,
# 		'drive_id':ply.drive_id,
# 		'time':ply.time,
# 		'pos_team':ply.pos_team,
# 		'yardline':ply.yardline,
# 		'down':ply.down,
# 		'yards_to_go':ply.yards_to_go,
# 		'description':ply.description,
# 		'note':ply.note,
# 		'':ply.,
# 		'':ply.,
# 		'':ply.,
#		'':ply.,
#		'':ply.,
#		'':ply.,
#		'':ply.,
#		'':ply.,
#		'':ply.,
#
# 	}
# 	return render(request, "play_view.html", context)

@csrf_exempt
def players_list(request):

	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		players = serializers.serialize('json',Player.objects.exclude(profile_url__isnull=True)[:5])
		json_players = json.loads(players)
		# return HttpResponse( players, content_type='application/json')
		return render(request, 'players.html', {'players_list':json_players})

def player_view(request, player_id):
	plyr = Player.objects.get(player_id=player_id)
	context = {
		'player_id':plyr.player_id,
		'gsis_name':plyr.gsis_name,
		'full_name':plyr.full_name,
		'team':plyr.team,
		'position':plyr.position,
		'profile_id':plyr.profile_id,
		'profile_url':plyr.profile_url,
		'uniform_number':plyr.uniform_number,
		'birthdate':plyr.birthdate,
		'college':plyr.college,
		'height':plyr.height,
		'weight':plyr.weight,
		'years_pro':plyr.years_pro,

	}
	return render(request, "player_view.html", context)

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
def teams_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		teams = serializers.serialize('json',Team.objects.all()[:10])
		json_teams = json.loads(teams)
		# return HttpResponse(games, content_type="application/json")
		return render(request, 'teams.html', {'teams_list':json_teams})

def team_view(request, team_id):
	tem = Team.objects.get(team_id=team_id)
	context = {
		'team_id':tem.team_id,
		'city':tem.city,
		'team_name':tem.name,

	}
	return render(request, "tem_view.html", context)

@csrf_exempt
def five_qb_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		# players = serializers.serialize('json',Game.objects.filter(season_year=2015, season_type='Regular')[:5])
		qbs = Player.objects.all()
		player_list = list(qbs)
		# qbs[Player]=[]
		# db = nfldb.connect()
		# q = nfldb.Query(db)
		# q.game(season_year=2015, season_type='Regular')
		# for g in q.sort('passing_yds').limit(5).as_aggregate():
		# 	qbs[Player] += [{
		# 		'id':g.player,
		# 		'yds':g.passing_yds,
		#
		# 	}]
		return JsonResponse(player_list,safe=False)
		# return HttpResponse(players, content_type="application/json")

	else:
		return HttpResponse("404")
		# return render(request, 'top.html',context)