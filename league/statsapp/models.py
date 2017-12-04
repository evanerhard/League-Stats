# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from django.utils.encoding import python_2_unicode_compatible

class AggPlay(models.Model):
    gsis = models.ForeignKey('Game', models.DO_NOTHING)
    drive_id = models.SmallIntegerField()
    play_id = models.SmallIntegerField()
    defense_ast = models.SmallIntegerField()
    defense_ffum = models.SmallIntegerField()
    defense_fgblk = models.SmallIntegerField()
    defense_frec = models.SmallIntegerField()
    defense_frec_tds = models.SmallIntegerField()
    defense_frec_yds = models.SmallIntegerField()
    defense_int = models.SmallIntegerField()
    defense_int_tds = models.SmallIntegerField()
    defense_int_yds = models.SmallIntegerField()
    defense_misc_tds = models.SmallIntegerField()
    defense_misc_yds = models.SmallIntegerField()
    defense_pass_def = models.SmallIntegerField()
    defense_puntblk = models.SmallIntegerField()
    defense_qbhit = models.SmallIntegerField()
    defense_safe = models.SmallIntegerField()
    defense_sk = models.FloatField()
    defense_sk_yds = models.SmallIntegerField()
    defense_tkl = models.SmallIntegerField()
    defense_tkl_loss = models.SmallIntegerField()
    defense_tkl_loss_yds = models.SmallIntegerField()
    defense_tkl_primary = models.SmallIntegerField()
    defense_xpblk = models.SmallIntegerField()
    fumbles_forced = models.SmallIntegerField()
    fumbles_lost = models.SmallIntegerField()
    fumbles_notforced = models.SmallIntegerField()
    fumbles_oob = models.SmallIntegerField()
    fumbles_rec = models.SmallIntegerField()
    fumbles_rec_tds = models.SmallIntegerField()
    fumbles_rec_yds = models.SmallIntegerField()
    fumbles_tot = models.SmallIntegerField()
    kicking_all_yds = models.SmallIntegerField()
    kicking_downed = models.SmallIntegerField()
    kicking_fga = models.SmallIntegerField()
    kicking_fgb = models.SmallIntegerField()
    kicking_fgm = models.SmallIntegerField()
    kicking_fgm_yds = models.SmallIntegerField()
    kicking_fgmissed = models.SmallIntegerField()
    kicking_fgmissed_yds = models.SmallIntegerField()
    kicking_i20 = models.SmallIntegerField()
    kicking_rec = models.SmallIntegerField()
    kicking_rec_tds = models.SmallIntegerField()
    kicking_tot = models.SmallIntegerField()
    kicking_touchback = models.SmallIntegerField()
    kicking_xpa = models.SmallIntegerField()
    kicking_xpb = models.SmallIntegerField()
    kicking_xpmade = models.SmallIntegerField()
    kicking_xpmissed = models.SmallIntegerField()
    kicking_yds = models.SmallIntegerField()
    kickret_fair = models.SmallIntegerField()
    kickret_oob = models.SmallIntegerField()
    kickret_ret = models.SmallIntegerField()
    kickret_tds = models.SmallIntegerField()
    kickret_touchback = models.SmallIntegerField()
    kickret_yds = models.SmallIntegerField()
    passing_att = models.SmallIntegerField()
    passing_cmp = models.SmallIntegerField()
    passing_cmp_air_yds = models.SmallIntegerField()
    passing_incmp = models.SmallIntegerField()
    passing_incmp_air_yds = models.SmallIntegerField()
    passing_int = models.SmallIntegerField()
    passing_sk = models.SmallIntegerField()
    passing_sk_yds = models.SmallIntegerField()
    passing_tds = models.SmallIntegerField()
    passing_twopta = models.SmallIntegerField()
    passing_twoptm = models.SmallIntegerField()
    passing_twoptmissed = models.SmallIntegerField()
    passing_yds = models.SmallIntegerField()
    punting_blk = models.SmallIntegerField()
    punting_i20 = models.SmallIntegerField()
    punting_tot = models.SmallIntegerField()
    punting_touchback = models.SmallIntegerField()
    punting_yds = models.SmallIntegerField()
    puntret_downed = models.SmallIntegerField()
    puntret_fair = models.SmallIntegerField()
    puntret_oob = models.SmallIntegerField()
    puntret_tds = models.SmallIntegerField()
    puntret_tot = models.SmallIntegerField()
    puntret_touchback = models.SmallIntegerField()
    puntret_yds = models.SmallIntegerField()
    receiving_rec = models.SmallIntegerField()
    receiving_tar = models.SmallIntegerField()
    receiving_tds = models.SmallIntegerField()
    receiving_twopta = models.SmallIntegerField()
    receiving_twoptm = models.SmallIntegerField()
    receiving_twoptmissed = models.SmallIntegerField()
    receiving_yac_yds = models.SmallIntegerField()
    receiving_yds = models.SmallIntegerField()
    rushing_att = models.SmallIntegerField()
    rushing_loss = models.SmallIntegerField()
    rushing_loss_yds = models.SmallIntegerField()
    rushing_tds = models.SmallIntegerField()
    rushing_twopta = models.SmallIntegerField()
    rushing_twoptm = models.SmallIntegerField()
    rushing_twoptmissed = models.SmallIntegerField()
    rushing_yds = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'agg_play'
        unique_together = (('gsis', 'drive_id', 'play_id'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drive(models.Model):
    gsis = models.ForeignKey('Game', models.DO_NOTHING)
    drive_id = models.SmallIntegerField(primary_key=True)
    start_time = models.TextField()  # This field type is a guess.
    start_field = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_field = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_time = models.TextField()  # This field type is a guess.
    pos_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='pos_team')
    pos_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_downs = models.SmallIntegerField()
    result = models.TextField(blank=True, null=True)
    penalty_yards = models.SmallIntegerField()
    yards_gained = models.SmallIntegerField()
    play_count = models.SmallIntegerField()
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'drive'
        unique_together = (('gsis', 'drive_id'),)


class Game(models.Model):
    gsis_id = models.CharField(primary_key=True, max_length=10)
    gamekey = models.CharField(max_length=5, blank=True, null=True)
    start_time = models.DateTimeField()
    week = models.SmallIntegerField()
    day_of_week = models.TextField()  # This field type is a guess.
    season_year = models.SmallIntegerField()
    season_type = models.TextField()  # This field type is a guess.
    finished = models.BooleanField()
    home_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='home_team',related_name='game_home_team')
    home_score = models.SmallIntegerField()
    home_score_q1 = models.SmallIntegerField(blank=True, null=True)
    home_score_q2 = models.SmallIntegerField(blank=True, null=True)
    home_score_q3 = models.SmallIntegerField(blank=True, null=True)
    home_score_q4 = models.SmallIntegerField(blank=True, null=True)
    home_score_q5 = models.SmallIntegerField(blank=True, null=True)
    home_turnovers = models.SmallIntegerField()
    away_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='away_team',related_name='game_away_team')
    away_score = models.SmallIntegerField()
    away_score_q1 = models.SmallIntegerField(blank=True, null=True)
    away_score_q2 = models.SmallIntegerField(blank=True, null=True)
    away_score_q3 = models.SmallIntegerField(blank=True, null=True)
    away_score_q4 = models.SmallIntegerField(blank=True, null=True)
    away_score_q5 = models.SmallIntegerField(blank=True, null=True)
    away_turnovers = models.SmallIntegerField()
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'game'

    def get_week(self):
        return self.week

class Meta(models.Model):
    # id = models.CharField(primary_key=True, max_length=10)
    version = models.SmallIntegerField(blank=True, null=True)
    last_roster_download = models.DateTimeField()
    season_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    season_year = models.SmallIntegerField(blank=True, null=True)
    week = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta'


class Play(models.Model):
    gsis = models.ForeignKey(Game, models.DO_NOTHING)
    play_id = models.SmallIntegerField(primary_key=True)
    drive_id = models.SmallIntegerField()
    time = models.TextField()  # This field type is a guess.
    pos_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='pos_team')
    yardline = models.TextField(blank=True, null=True)  # This field type is a guess.
    down = models.SmallIntegerField(blank=True, null=True)
    yards_to_go = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()
    first_down = models.SmallIntegerField()
    fourth_down_att = models.SmallIntegerField()
    fourth_down_conv = models.SmallIntegerField()
    fourth_down_failed = models.SmallIntegerField()
    passing_first_down = models.SmallIntegerField()
    penalty = models.SmallIntegerField()
    penalty_first_down = models.SmallIntegerField()
    penalty_yds = models.SmallIntegerField()
    rushing_first_down = models.SmallIntegerField()
    third_down_att = models.SmallIntegerField()
    third_down_conv = models.SmallIntegerField()
    third_down_failed = models.SmallIntegerField()
    timeout = models.SmallIntegerField()
    xp_aborted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'play'
        unique_together = (('gsis', 'drive_id', 'play_id'),)


class PlayPlayer(models.Model):
    gsis = models.ForeignKey(Game, models.DO_NOTHING)
    drive_id = models.SmallIntegerField()
    play_id = models.SmallIntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team')
    defense_ast = models.SmallIntegerField()
    defense_ffum = models.SmallIntegerField()
    defense_fgblk = models.SmallIntegerField()
    defense_frec = models.SmallIntegerField()
    defense_frec_tds = models.SmallIntegerField()
    defense_frec_yds = models.SmallIntegerField()
    defense_int = models.SmallIntegerField()
    defense_int_tds = models.SmallIntegerField()
    defense_int_yds = models.SmallIntegerField()
    defense_misc_tds = models.SmallIntegerField()
    defense_misc_yds = models.SmallIntegerField()
    defense_pass_def = models.SmallIntegerField()
    defense_puntblk = models.SmallIntegerField()
    defense_qbhit = models.SmallIntegerField()
    defense_safe = models.SmallIntegerField()
    defense_sk = models.FloatField()
    defense_sk_yds = models.SmallIntegerField()
    defense_tkl = models.SmallIntegerField()
    defense_tkl_loss = models.SmallIntegerField()
    defense_tkl_loss_yds = models.SmallIntegerField()
    defense_tkl_primary = models.SmallIntegerField()
    defense_xpblk = models.SmallIntegerField()
    fumbles_forced = models.SmallIntegerField()
    fumbles_lost = models.SmallIntegerField()
    fumbles_notforced = models.SmallIntegerField()
    fumbles_oob = models.SmallIntegerField()
    fumbles_rec = models.SmallIntegerField()
    fumbles_rec_tds = models.SmallIntegerField()
    fumbles_rec_yds = models.SmallIntegerField()
    fumbles_tot = models.SmallIntegerField()
    kicking_all_yds = models.SmallIntegerField()
    kicking_downed = models.SmallIntegerField()
    kicking_fga = models.SmallIntegerField()
    kicking_fgb = models.SmallIntegerField()
    kicking_fgm = models.SmallIntegerField()
    kicking_fgm_yds = models.SmallIntegerField()
    kicking_fgmissed = models.SmallIntegerField()
    kicking_fgmissed_yds = models.SmallIntegerField()
    kicking_i20 = models.SmallIntegerField()
    kicking_rec = models.SmallIntegerField()
    kicking_rec_tds = models.SmallIntegerField()
    kicking_tot = models.SmallIntegerField()
    kicking_touchback = models.SmallIntegerField()
    kicking_xpa = models.SmallIntegerField()
    kicking_xpb = models.SmallIntegerField()
    kicking_xpmade = models.SmallIntegerField()
    kicking_xpmissed = models.SmallIntegerField()
    kicking_yds = models.SmallIntegerField()
    kickret_fair = models.SmallIntegerField()
    kickret_oob = models.SmallIntegerField()
    kickret_ret = models.SmallIntegerField()
    kickret_tds = models.SmallIntegerField()
    kickret_touchback = models.SmallIntegerField()
    kickret_yds = models.SmallIntegerField()
    passing_att = models.SmallIntegerField()
    passing_cmp = models.SmallIntegerField()
    passing_cmp_air_yds = models.SmallIntegerField()
    passing_incmp = models.SmallIntegerField()
    passing_incmp_air_yds = models.SmallIntegerField()
    passing_int = models.SmallIntegerField()
    passing_sk = models.SmallIntegerField()
    passing_sk_yds = models.SmallIntegerField()
    passing_tds = models.SmallIntegerField()
    passing_twopta = models.SmallIntegerField()
    passing_twoptm = models.SmallIntegerField()
    passing_twoptmissed = models.SmallIntegerField()
    passing_yds = models.SmallIntegerField()
    punting_blk = models.SmallIntegerField()
    punting_i20 = models.SmallIntegerField()
    punting_tot = models.SmallIntegerField()
    punting_touchback = models.SmallIntegerField()
    punting_yds = models.SmallIntegerField()
    puntret_downed = models.SmallIntegerField()
    puntret_fair = models.SmallIntegerField()
    puntret_oob = models.SmallIntegerField()
    puntret_tds = models.SmallIntegerField()
    puntret_tot = models.SmallIntegerField()
    puntret_touchback = models.SmallIntegerField()
    puntret_yds = models.SmallIntegerField()
    receiving_rec = models.SmallIntegerField()
    receiving_tar = models.SmallIntegerField()
    receiving_tds = models.SmallIntegerField()
    receiving_twopta = models.SmallIntegerField()
    receiving_twoptm = models.SmallIntegerField()
    receiving_twoptmissed = models.SmallIntegerField()
    receiving_yac_yds = models.SmallIntegerField()
    receiving_yds = models.SmallIntegerField()
    rushing_att = models.SmallIntegerField()
    rushing_loss = models.SmallIntegerField()
    rushing_loss_yds = models.SmallIntegerField()
    rushing_tds = models.SmallIntegerField()
    rushing_twopta = models.SmallIntegerField()
    rushing_twoptm = models.SmallIntegerField()
    rushing_twoptmissed = models.SmallIntegerField()
    rushing_yds = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'play_player'
        unique_together = (('gsis', 'drive_id', 'play_id', 'player'),)

@python_2_unicode_compatible
class Player(models.Model):
    player_id = models.CharField(primary_key=True, max_length=10)
    gsis_name = models.CharField(max_length=75, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team')
    position = models.TextField()  # This field type is a guess.
    profile_id = models.IntegerField(blank=True, null=True)
    profile_url = models.CharField(max_length=255, blank=True, null=True)
    uniform_number = models.SmallIntegerField(blank=True, null=True)
    birthdate = models.CharField(max_length=75, blank=True, null=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    years_pro = models.SmallIntegerField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'player'

    def get_absolute_url(self):
        return reverse('players',kwargs={'pk':self.player_id})

    def __str__(self):
        if self.full_name == None:
            return str(self.gsis_name)
        else:
            return str(self.full_name)

    def __unicode__(self):
        if self.full_name == None:
            return str(self.gsis_name)
        else:
            return str(self.full_name)

    def get_position(self):
        if str(self.position) == 'QB':
            return "QuarterBack(QB)"
        elif str(self.position) == 'WR':
            return "Wide Receiver(WR)"
        elif str(self.position) == 'TE':
            return "Tight End(TE)"
        elif str(self.position) == 'RB':
            return "RunningBack(RB)"
        elif str(self.position) == 'FB':
            return "FullBack(FB)"
        elif str(self.position) == 'LT':
            return "Left Tackle(LT)"
        elif str(self.position) == 'LG':
            return "Left Guard(LG)"
        elif str(self.position) == 'C':
            return "Center(C)"
        elif str(self.position) == 'RG':
            return "Right Guard(RG)"
        elif str(self.position) == 'RT':
            return "Right Tackle(RT)"
        elif str(self.position) == 'DE':
            return "Defensive End(DE)"
        elif str(self.position) == 'DT' :
            return "Defensive Tackle(DT"
        elif str(self.position) == 'OLB':
            return "Outside LineBacker(OLB)"
        elif str(self.position) == 'ILB':
            return "Inside LineBacker(ILB)"
        elif str(self.position) == 'CB':
            return "CornerBack(CB)"
        elif str(self.position) == 'SS':
            return "Strong Safety(SS)"
        elif str(self.position) == 'FS':
            return "Free Safety(FS)"
        elif str(self.position) == 'K':
            return "Kicker(K)"
        elif str(self.position) == 'P':
            return "Punter(P)"
        elif str(self.position) == 'KR':
            return "Kick Returner(KR)"
        elif str(self.position) == 'PR':
            return "Punt Returner(PR)"
        else:
            return str(self.position)

    def get_team(self):
        if self.team == None:
            return 'NA'
        if self.team == 'ARI':
            return "Arizona Cardinals"
        elif self.team == 'ATL':
            return "Atlanta Falcons"
        elif self.team == 'BAl':
            return "Baltimore Ravens"
        elif self.team == 'BUF':
            return "Buffalo Bills"
        elif self.team == 'CAR':
            return "Carolina Panthers"
        elif self.team == 'CHI':
            return "Chicago Bears"
        elif self.team == 'CIN':
            return "Cincinnati Bengals"
        elif self.team == 'CLE':
            return "Cleveland Browns"
        elif self.team == 'DAL':
            return "Dallas Cowboys"
        elif self.team == 'DEN':
            return "Denver Broncos"
        elif self.team == 'DET':
            return "Detroit Lions"
        elif self.team == 'GB':
            return "Green Bay Packers"
        elif self.team == 'HOU':
            return "Houston Texans"
        elif self.team == 'IND':
            return "Indianapolis Colts"
        elif self.team == 'JAC':
            return "Jacksonville Jaguars"
        elif self.team == 'KC':
            return "Kansas City Chiefs"
        elif self.team == 'MIA':
            return "Miami Dolphins"
        elif self.team == 'MIN':
            return "Minnesota Vikings"
        elif self.team == 'NE':
            return "New England Patriots"
        elif self.team == 'NO':
            return "New Orleans Saints"
        elif self.team == 'OAK':
            return "Oakland Raiders"
        elif self.team == 'PHI':
            return "Philadelphia Eagles"
        elif self.team == 'PIT':
            return "Pittsburgh Steelers"
        elif self.team == 'SD':
            return "San Diego Chargers"
        elif self.team == 'SEA':
            return "Seattle Seahawks"
        elif self.team == 'SF':
            return "San Francisco 49ers"
        elif self.team == 'STL':
            return "St. Louis Rams"
        elif self.team == 'TB':
            return "Tampa Bay Buccaneers"
        elif self.team == 'TEN':
            return "Tennessee Titans"
        elif self.team == 'WAS':
            return "Washington Redskins"
        elif self.team == 'NYG':
            return "New York Giants"
        elif self.team == 'NYJ':
            return "New York Jets"
        elif self.team == 'LA':
            return "Los Angeles Rams"
        elif self.team == 'JAX':
            return "Jacksonville Jaguars"
        elif self.team == 'LAC':
            return "Los Angeles Chargers"
        else:
            return str(self.team)
    def get_years_pro(self):
        return self.years_pro

@python_2_unicode_compatible
class Team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=3)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'team'

    def __str__(self):
        return str(self.team_id)

    def __unicode__(self):
        return str(self.team_id)

    def get_team_id(self):
        return self.team_id
    def get_team_city(self):
        return self.city
    def get_team_name(self):
        return self.name

# @python_2_unicode_compatible
# class
