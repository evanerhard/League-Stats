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
import sys

O_Positions = ['QB', 'RB', 'FB', 'LT', 'LG', 'C', 'RG', 'RT', 'TE','WR' ]
D_Positions = ['DE', 'DT', 'OLB', 'ILB', 'CB', 'SS', 'FS']
S_Positions = ['K', 'P', 'KR', 'PR']

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
		games = serializers.serialize('json',Game.objects.filter(season_year=2017).order_by('week'))
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
		players = serializers.serialize('json',Player.objects.exclude(years_pro__isnull=True)[:1000])
		json_players = json.loads(players)
		# return HttpResponse( players, content_type='application/json')
		return render(request, 'players.html', {'players_list':json_players})

def player_view(request, player_id):
	plyr = Player.objects.get(player_id=player_id)
	posit = plyr.get_position()
	team_name = plyr.team.get_team_name()
	team_city = plyr.team.get_team_city()
	context = {
		'player_id':plyr.player_id,
		'gsis_name':plyr.gsis_name,
		'full_name':plyr.full_name,
		'teamcity':team_city,
		'teamname':team_name,
		'posit':posit,
		'position':str(plyr.position),
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

def catches_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		catchperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()
		drives = q.drive(pos_team=team).sort(('start_time', 'asc')).as_drives()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			catchperweek[w] = []
		weeks.sort(key=int)
		for d in drives:
		    catch = 0
		    for w in weeks:
			    q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
			    q.player(full_name=name)
			    q.game(week=w)
			    results = q.aggregate(receiving_rec__ge=0).as_aggregate()
			    if len(results) == 0:
			        continue
			    tfb = results[0]
			    catch += tfb.receiving_rec

		    for w in weeks:
		    	 if w == d.game.week:
	        		catchperweek[w] += [catch]

		for w in weeks:
			catchperweek[w] = sum(catchperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'catches_per_week':catchperweek,
		}
		return render(request, "player_catch.html", {'data':data})


def passing_yds_player(request, player_id):
	if request.method == "POST":
		return HttpResponse('Cannot POST.')
	if request.method == "GET":
		db = nfldb.connect()
		q = nfldb.Query(db)
		data = {}
		player = Player.objects.get(player_id=player_id)
		name = str(player)
		team = player.get_team()
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		passydperweek = {}

		games = q.game(season_year=2017, season_type='Regular', team=team).as_games()
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
			'team_name':team_name,
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
		team_name = player.team.get_team_name()
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
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'rushing_per_week':rushydperweek,
		}
		return render(request, "player_rushing.html", {'data':data})

def receiving_yds_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		receivingydperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()
		drives = q.drive(pos_team=team).sort(('start_time', 'asc')).as_drives()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			receivingydperweek[w] = []
		weeks.sort(key=int)
		for d in drives:
		    receive_yds = 0
		    for w in weeks:
			    q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
			    q.player(full_name=name)
			    q.game(week=w)
			    results = q.aggregate(receiving_yds__ge=0).as_aggregate()
			    if len(results) == 0:
			        continue
			    tfb = results[0]
			    receive_yds += tfb.receiving_yds

		    for w in weeks:
		    	 if w == d.game.week:
	        		receivingydperweek[w] += [receive_yds]

		for w in weeks:
			receivingydperweek[w] = sum(receivingydperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'receiving_per_week':receivingydperweek,
		}
		return render(request, "player_receiving.html", {'data':data})

def sacks_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		sackperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			sackperweek[w] = []
		weeks.sort(key=int)

		for g in games:
			sacks = 0
			q = nfldb.Query(db).play(gsis_id=g.gsis_id)
			plays = q.player(full_name=name).as_plays()
			for p in plays:
				results = p.defense_sk
				sacks += results
				#print results

			for w in weeks:
				if w == g.week:
					sackperweek[w] += [sacks]

		for w in weeks:
			sackperweek[w] = sum(sackperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'sacks_per_week':sackperweek,
		}
		return render(request, "player_sack.html", {'data':data})

def tackles_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		tackleperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			tackleperweek[w] = []
		weeks.sort(key=int)

		for g in games:
			tackles = 0
			q = nfldb.Query(db).play(gsis_id=g.gsis_id)
			plays = q.player(full_name=name).as_plays()
			for p in plays:
				results = p.defense_tkl
				tackles += results

			for w in weeks:
				if w == g.week:
					tackleperweek[w] += [tackles]

		for w in weeks:
			tackleperweek[w] = sum(tackleperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'tackles_per_week':tackleperweek,
		}
		return render(request, "player_tackle.html", {'data':data})

def picks_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		pickperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			pickperweek[w] = []
		weeks.sort(key=int)

		for g in games:
			picks = 0
			q = nfldb.Query(db).play(gsis_id=g.gsis_id)
			plays = q.player(full_name=name).as_plays()
			for p in plays:
				results = p.defense_int
				picks += results
				# print picks
				# print p

			for w in weeks:
				if w == g.week:
					pickperweek[w] += [picks]

		for w in weeks:
			pickperweek[w] = sum(pickperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'picks_per_week':pickperweek,
		}
		return render(request, "player_picks.html", {'data':data})

def passblock_player(request, player_id):
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
		team_name = player.team.get_team_name()
		position = player.get_position()
		weeks = []
		blkperweek = {}

		games = q.game(season_year=seas_year, season_type='Regular', team=team).as_games()

		for i in range(0,len(games)):
			if games[i].finished:
				weeks.append(games[i].week)

		for w in weeks:
			blkperweek[w] = []
		weeks.sort(key=int)

		for g in games:
			blocks = 0
			q = nfldb.Query(db).play(gsis_id=g.gsis_id)
			plays = q.player(full_name=name).as_plays()
			for p in plays:
				results = p.defense_pass_def
				blocks += results
				# print picks
				# print p

			for w in weeks:
				if w == g.week:
					blkperweek[w] += [blocks]

		for w in weeks:
			blkperweek[w] = sum(blkperweek[w])

		data = {
			'player':player,
			'player_id':player_id,
			'name':name,
			'team':team,
			'team_name':team_name,
			'position':position,
			'weeks':weeks,
			'blocks_per_week':blkperweek,
		}
		return render(request, "player_blocks.html", {'data':data})

def search_player(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			db = nfldb.connect()
			s_position = form.cleaned_data['position']
			s_name = form.cleaned_data['full_name']
			s_team = form.cleaned_data['team']
			player = None
			if s_team == 'None' and s_position == 'None':
				players = Player.objects.filter(full_name__contains=s_name)
				player, s_score = nfldb.player_search(db, s_name)
				#print 'Similarity score: %d, Player: %s' % (s_score, players)
			elif s_name == '' and s_position == 'None':
				players = Player.objects.filter(team=s_team)
			elif s_team == 'None' and s_name == '':
				players = Player.objects.filter(position=s_position)
			elif s_team == 'None':
				players = Player.objects.filter(position=s_position,full_name__contains=s_name)
				player, s_score = nfldb.player_search(db, s_name)
			else:
				players = Player.objects.filter(team=s_team,position=s_position,full_name__contains=s_name)
				player, s_score = nfldb.player_search(db, s_name)
			if len(players) ==1:
				link_id = player.player_id
				link_s = '/players/'
				link = link_s + link_id
				return HttpResponseRedirect(link)

			return render(request, "search_player.html", {'form':form,'players':players,'player':player})

	else:
		form = SearchForm()
	return render(request, "search_player.html", {'form':form})

# QB_STATS = ('passing_yds','rushing_yds')
# RB_STATS = ('rushing_yds')
# WR_STATS = ('receiving_yds')
# FB_STATS = ('rushing_yds')
def compare_players(request):
	if request.method == 'POST':
		form = CompareForm(request.POST)
		if form.is_valid():
			db = nfldb.connect()
			seas_year = 2017
			weeks = []
			passydperweek1 = {}
			passydperweek2 = {}
			s_position = form.cleaned_data['position']
			s_player1 = form.cleaned_data['full_name_1']
			s_player2 = form.cleaned_data['full_name_2']

			players = Player.objects.exclude(team='UNK') & Player.objects.filter(position=s_position)
			player1,s_score1 = nfldb.player_search(db,s_player1)
			player2,s_score2 = nfldb.player_search(db,s_player2)
			fullname1 = str(player1.full_name)
			fullname2 = str(player2.full_name)
			team1 = str(player1.team)
			team2 = str(player2.team)
			q = nfldb.Query(db)
			games1 = q.game(season_year=seas_year, season_type='Regular', team=team1).as_games()
			drives1 = q.drive(pos_team=team1).sort(('start_time', 'asc')).as_drives()
			games2 = q.game(season_year=seas_year, season_type='Regular', team=team2).as_games()
			drives2 = q.drive(pos_team=team2).sort(('start_time', 'asc')).as_drives()

			for i in range(0,len(games1)):
				if games1[i].finished:
					weeks.append(games1[i].week)
			for w in weeks:
				passydperweek1[w] = []
				passydperweek2[w] = []
			weeks.sort(key=int)
			#for loop for the first player.
			for d in drives1:
				pass_yds = 0
	 			for w in weeks:
	 				q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
	 				q.player(full_name=fullname1)
	 				q.game(week=w)
	 				results = q.aggregate(passing_yds__ge=0).as_aggregate()
	 				if len(results) == 0:
	 					continue
	 				tfb = results[0]
	 				pass_yds += tfb.passing_yds
	 			for w in weeks:
	 				if w == d.game.week:
	 					passydperweek1[w] += [pass_yds]
			for w in weeks:
				passydperweek1[w] = sum(passydperweek1[w])

			q2 = nfldb.Query(db)
			games2 = q2.game(season_year=seas_year, season_type='Regular', team=team2).as_games()
			drives2 = q2.drive(pos_team=team2).sort(('start_time', 'asc')).as_drives()
			#for loop for second player.
			for d in drives2:
				pass_yds = 0
				#print d
	 			for w in weeks:
	 				q = nfldb.Query(db).drive(gsis_id=d.gsis_id, drive_id=d.drive_id)
	 				q.player(full_name=fullname2)
	 				q.game(week=w)
	 				results = q.aggregate(passing_yds__ge=0).as_aggregate()
	 				if len(results) == 0:
	 					continue
	 				tfb = results[0]
	 				pass_yds += tfb.passing_yds
	 			for w in weeks:
	 				if w == d.game.week:
	 					passydperweek2[w] += [pass_yds]
			for w in weeks:
				passydperweek2[w] = sum(passydperweek2[w])


			data = {
				'form':form,
				'player1':player1,
				'player2':player2,
				'weeks':weeks,
				'team1':team1,
				'team2':team2,
				'passydperweek1':passydperweek1,
				'passydperweek2':passydperweek2,
			}
			return render(request, "compare_players.html", {'data':data})

	else:
		form = CompareForm()
	return render(request, "compare_players.html", {'form':form})

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
