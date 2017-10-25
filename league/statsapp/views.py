from django.shortcuts import render,HttpResponse, HttpResponseRedirect, get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.views import generic

from .models import *
from .forms import *

import json
import nfldb
import time

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
		games = serializers.serialize('json',Game.objects.filter(season_year=2017))
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

def passing_per_playr(request, player_id):
	if request.method == "POST":
		return HttpREsponse('Cannot POST here.')
	if request.method == "GET":
		# passing = serializers.serialize('json', Player.objects.get(player_id=player_id))
		passing_plyr = Player.objects.get(player_id=player_id)

	else:
		return HttpResponse("404")

@csrf_exempt
def play_list(request):

	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		plays = serializers.serialize('json',Play.objects.all()[:10])
		json_plays = json.loads(plays)
		# return HttpResponse( players, content_type='application/json')
		return render(request, 'plays.html', {'plays_list':json_plays})

@csrf_exempt
def players_list(request):

	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		players = serializers.serialize('json',Player.objects.exclude(years_pro__isnull=True)[:50])
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
	def if_qb(self):
		if self.position == "QB":
			return True
		else:
			return False

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
def rookies_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		players = serializers.serialize('json',Player.objects.exclude(profile_url__isnull=True,years_pro=0,  full_name=None)[:50])
		json_players = json.loads(players)
		# return HttpResponse( players, content_type='application/json')
		return render(request, 'players.html', {'players_list':json_players})

@csrf_exempt
def teams_list(request):
	if request.method == "POST":
		return HttpResponse('POST Successful.')
	if request.method == "GET":
		# teams = serializers.serialize('json',Team.objects.all()[:10])
		teams = serializers.serialize('json',Team.objects.all())
		json_teams = json.loads(teams)
		# return HttpResponse(games, content_type="application/json")
		return render(request, 'teams.html', {'teams_list':json_teams})

def team_view(request, team_id):
	tem = Team.objects.get(team_id=team_id)
	context = {
		'team_id':tem.team_id,
		'team_city':tem.city,
		'team_name':tem.name,
	}
	return render(request, "team_view.html", context)

@csrf_exempt
def five_qb_list(request):
	if request.method == "POST":
		return HttpResponse('Cannot POST.')
	if request.method == "GET":
		qbs = {}
		qbs['passing']=[]
		db = nfldb.connect()
		q = nfldb.Query(db)
		q.game(season_year=2017, season_type='Regular')
		for g in q.sort('passing_yds').limit(5).as_aggregate():
			qbs['passing'] += [{
				'id':g.player.player_id,
				'name':g.player.full_name,
				'yds':g.passing_yds,

			}]
			# print(g)
		# qbs = serializers.serialize(qbs)
		# return JsonResponse(qbs)
		# return HttpResponse(players, content_type="application/json")
		return render(request, "top.html", {'pass_list':qbs['passing']})

	else:
		return HttpResponse("404")

def passing_yds_player(request, player_id,season_year):
	if request.method == "POST":
		return HttpResponse('Cannot POST.')
	if request.method == "GET":
		db = nfldb.connect()
		q = nfldb.Query(db)
		data = {}
		player = Player.objects.get(player_id=player_id)
		name = str(player)
		team = player.get_team()
		position = player.get_position()
		weeks = []
		passydperweek = {}

		games = q.game(season_year=season_year, season_type='Regular', team=team).as_games()
		drives = q.drive(pos_team=team).sort(('start_time', 'asc')).as_drives()
		# tpl = 'On drive {drive_num}, {name} went {cmp}/{att} for {yds} yard(s) ' \
		#       'with {tds} TD(s), {int} INT(s) and was sacked {sack} time(s).'
		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)
				#weeks.append(i)

		for w in weeks:
			passydperweek[w] = []
		weeks.sort(key=int)
		for d in drives:
		    pass_yds = 0
		    for w in weeks:
			    q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
			    q.player(full_name=name)
			    q.game(week=w)
			    results = q.aggregate(passing_yds__ge=0).as_aggregate()
			    if len(results) == 0:
			        continue
			    tfb = results[0]
			    pass_yds += tfb.passing_yds
		    # msg = tpl.format(drive_num=i+1,name=name, cmp=tfb.passing_cmp, att=tfb.passing_att,
		    #                  yds=tfb.passing_yds, tds=tfb.passing_tds,
		    #                  int=tfb.passing_int, sack=tfb.passing_sk)
		    for w in weeks:
		    	 if w == d.game.week:
	        		passydperweek[w] += [pass_yds]
	    		#print "it worked."
		    #print d.game.week
		    x = pass_yds

		for w in weeks:
			passydperweek[w] = sum(passydperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'position':position,
			'weeks':weeks,
			'passing_per_week':passydperweek,
		}
		return render(request, "player_passing.html", {'data':data})

def rushing_yds_player(request, player_id):
	if request.method == "POST":
		return HttpResponse('Cannot POST.')
	if request.method == "GET":
		db = nfldb.connect()
		q = nfldb.Query(db)
		data = {}
		seas_year = '2017'
		player = Player.objects.get(player_id=player_id)
		name = str(player)
		team = player.get_team()
		position = player.get_position()
		weeks = []
		rushydperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()
		drives = q.drive(pos_team=team).sort(('start_time', 'asc')).as_drives()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			rushydperweek[w] = []
		weeks.sort(key=int)
		for d in drives:
		    rush_yds = 0
		    for w in weeks:
			    q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
			    q.player(full_name=name)
			    q.game(week=w)
			    results = q.aggregate(rushing_yds__ge=0).as_aggregate()
			    if len(results) == 0:
			        continue
			    tfb = results[0]
			    rush_yds += tfb.rushing_yds

		    for w in weeks:
		    	 if w == d.game.week:
	        		rushydperweek[w] += [rush_yds]

		for w in weeks:
			rushydperweek[w] = sum(rushydperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'position':position,
			'weeks':weeks,
			'rushing_per_week':rushydperweek,
		}
		return render(request, "player_rushing.html", {'data':data})

def search_player(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			s_position = form.cleaned_data['position']
			s_name = form.cleaned_data['full_name']
			players = Player.objects.filter(full_name__contains=s_name,position=s_position)

			return render(request, "search_player.html", {'form':form,'players':players})

	else:
		form = SearchForm()
	return render(request, "search_player.html", {'form':form})


class SearchResults(generic.ListView):
	template_name = 'results.html'

	def get_queryset(self):
		return Player.objects.all()[:50]

def chart_example(request, *args, **kwargs):
	stat_data = []
	year_data = []

	year_data = ['2000','2001','2002','2003','2004','2005']
	stat_data = [1.234, 12, 12.34, 15, 7.8, 9.5]

	data = {
		'year_data':year_data,
		'stat_data':stat_data,
	}

	return render(request, "chart_example.html", data)
