# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-24 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AggPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_id', models.SmallIntegerField()),
                ('play_id', models.SmallIntegerField()),
                ('defense_ast', models.SmallIntegerField()),
                ('defense_ffum', models.SmallIntegerField()),
                ('defense_fgblk', models.SmallIntegerField()),
                ('defense_frec', models.SmallIntegerField()),
                ('defense_frec_tds', models.SmallIntegerField()),
                ('defense_frec_yds', models.SmallIntegerField()),
                ('defense_int', models.SmallIntegerField()),
                ('defense_int_tds', models.SmallIntegerField()),
                ('defense_int_yds', models.SmallIntegerField()),
                ('defense_misc_tds', models.SmallIntegerField()),
                ('defense_misc_yds', models.SmallIntegerField()),
                ('defense_pass_def', models.SmallIntegerField()),
                ('defense_puntblk', models.SmallIntegerField()),
                ('defense_qbhit', models.SmallIntegerField()),
                ('defense_safe', models.SmallIntegerField()),
                ('defense_sk', models.FloatField()),
                ('defense_sk_yds', models.SmallIntegerField()),
                ('defense_tkl', models.SmallIntegerField()),
                ('defense_tkl_loss', models.SmallIntegerField()),
                ('defense_tkl_loss_yds', models.SmallIntegerField()),
                ('defense_tkl_primary', models.SmallIntegerField()),
                ('defense_xpblk', models.SmallIntegerField()),
                ('fumbles_forced', models.SmallIntegerField()),
                ('fumbles_lost', models.SmallIntegerField()),
                ('fumbles_notforced', models.SmallIntegerField()),
                ('fumbles_oob', models.SmallIntegerField()),
                ('fumbles_rec', models.SmallIntegerField()),
                ('fumbles_rec_tds', models.SmallIntegerField()),
                ('fumbles_rec_yds', models.SmallIntegerField()),
                ('fumbles_tot', models.SmallIntegerField()),
                ('kicking_all_yds', models.SmallIntegerField()),
                ('kicking_downed', models.SmallIntegerField()),
                ('kicking_fga', models.SmallIntegerField()),
                ('kicking_fgb', models.SmallIntegerField()),
                ('kicking_fgm', models.SmallIntegerField()),
                ('kicking_fgm_yds', models.SmallIntegerField()),
                ('kicking_fgmissed', models.SmallIntegerField()),
                ('kicking_fgmissed_yds', models.SmallIntegerField()),
                ('kicking_i20', models.SmallIntegerField()),
                ('kicking_rec', models.SmallIntegerField()),
                ('kicking_rec_tds', models.SmallIntegerField()),
                ('kicking_tot', models.SmallIntegerField()),
                ('kicking_touchback', models.SmallIntegerField()),
                ('kicking_xpa', models.SmallIntegerField()),
                ('kicking_xpb', models.SmallIntegerField()),
                ('kicking_xpmade', models.SmallIntegerField()),
                ('kicking_xpmissed', models.SmallIntegerField()),
                ('kicking_yds', models.SmallIntegerField()),
                ('kickret_fair', models.SmallIntegerField()),
                ('kickret_oob', models.SmallIntegerField()),
                ('kickret_ret', models.SmallIntegerField()),
                ('kickret_tds', models.SmallIntegerField()),
                ('kickret_touchback', models.SmallIntegerField()),
                ('kickret_yds', models.SmallIntegerField()),
                ('passing_att', models.SmallIntegerField()),
                ('passing_cmp', models.SmallIntegerField()),
                ('passing_cmp_air_yds', models.SmallIntegerField()),
                ('passing_incmp', models.SmallIntegerField()),
                ('passing_incmp_air_yds', models.SmallIntegerField()),
                ('passing_int', models.SmallIntegerField()),
                ('passing_sk', models.SmallIntegerField()),
                ('passing_sk_yds', models.SmallIntegerField()),
                ('passing_tds', models.SmallIntegerField()),
                ('passing_twopta', models.SmallIntegerField()),
                ('passing_twoptm', models.SmallIntegerField()),
                ('passing_twoptmissed', models.SmallIntegerField()),
                ('passing_yds', models.SmallIntegerField()),
                ('punting_blk', models.SmallIntegerField()),
                ('punting_i20', models.SmallIntegerField()),
                ('punting_tot', models.SmallIntegerField()),
                ('punting_touchback', models.SmallIntegerField()),
                ('punting_yds', models.SmallIntegerField()),
                ('puntret_downed', models.SmallIntegerField()),
                ('puntret_fair', models.SmallIntegerField()),
                ('puntret_oob', models.SmallIntegerField()),
                ('puntret_tds', models.SmallIntegerField()),
                ('puntret_tot', models.SmallIntegerField()),
                ('puntret_touchback', models.SmallIntegerField()),
                ('puntret_yds', models.SmallIntegerField()),
                ('receiving_rec', models.SmallIntegerField()),
                ('receiving_tar', models.SmallIntegerField()),
                ('receiving_tds', models.SmallIntegerField()),
                ('receiving_twopta', models.SmallIntegerField()),
                ('receiving_twoptm', models.SmallIntegerField()),
                ('receiving_twoptmissed', models.SmallIntegerField()),
                ('receiving_yac_yds', models.SmallIntegerField()),
                ('receiving_yds', models.SmallIntegerField()),
                ('rushing_att', models.SmallIntegerField()),
                ('rushing_loss', models.SmallIntegerField()),
                ('rushing_loss_yds', models.SmallIntegerField()),
                ('rushing_tds', models.SmallIntegerField()),
                ('rushing_twopta', models.SmallIntegerField()),
                ('rushing_twoptm', models.SmallIntegerField()),
                ('rushing_twoptmissed', models.SmallIntegerField()),
                ('rushing_yds', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'agg_play',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('drive_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('start_time', models.TextField()),
                ('start_field', models.TextField(blank=True, null=True)),
                ('end_field', models.TextField(blank=True, null=True)),
                ('end_time', models.TextField()),
                ('pos_time', models.TextField(blank=True, null=True)),
                ('first_downs', models.SmallIntegerField()),
                ('result', models.TextField(blank=True, null=True)),
                ('penalty_yards', models.SmallIntegerField()),
                ('yards_gained', models.SmallIntegerField()),
                ('play_count', models.SmallIntegerField()),
                ('time_inserted', models.DateTimeField()),
                ('time_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'drive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('gsis_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gamekey', models.CharField(blank=True, max_length=5, null=True)),
                ('start_time', models.DateTimeField()),
                ('week', models.SmallIntegerField()),
                ('day_of_week', models.TextField()),
                ('season_year', models.SmallIntegerField()),
                ('season_type', models.TextField()),
                ('finished', models.BooleanField()),
                ('home_score', models.SmallIntegerField()),
                ('home_score_q1', models.SmallIntegerField(blank=True, null=True)),
                ('home_score_q2', models.SmallIntegerField(blank=True, null=True)),
                ('home_score_q3', models.SmallIntegerField(blank=True, null=True)),
                ('home_score_q4', models.SmallIntegerField(blank=True, null=True)),
                ('home_score_q5', models.SmallIntegerField(blank=True, null=True)),
                ('home_turnovers', models.SmallIntegerField()),
                ('away_score', models.SmallIntegerField()),
                ('away_score_q1', models.SmallIntegerField(blank=True, null=True)),
                ('away_score_q2', models.SmallIntegerField(blank=True, null=True)),
                ('away_score_q3', models.SmallIntegerField(blank=True, null=True)),
                ('away_score_q4', models.SmallIntegerField(blank=True, null=True)),
                ('away_score_q5', models.SmallIntegerField(blank=True, null=True)),
                ('away_turnovers', models.SmallIntegerField()),
                ('time_inserted', models.DateTimeField()),
                ('time_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.SmallIntegerField(blank=True, null=True)),
                ('last_roster_download', models.DateTimeField()),
                ('season_type', models.TextField(blank=True, null=True)),
                ('season_year', models.SmallIntegerField(blank=True, null=True)),
                ('week', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'meta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('play_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('drive_id', models.SmallIntegerField()),
                ('time', models.TextField()),
                ('yardline', models.TextField(blank=True, null=True)),
                ('down', models.SmallIntegerField(blank=True, null=True)),
                ('yards_to_go', models.SmallIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('time_inserted', models.DateTimeField()),
                ('time_updated', models.DateTimeField()),
                ('first_down', models.SmallIntegerField()),
                ('fourth_down_att', models.SmallIntegerField()),
                ('fourth_down_conv', models.SmallIntegerField()),
                ('fourth_down_failed', models.SmallIntegerField()),
                ('passing_first_down', models.SmallIntegerField()),
                ('penalty', models.SmallIntegerField()),
                ('penalty_first_down', models.SmallIntegerField()),
                ('penalty_yds', models.SmallIntegerField()),
                ('rushing_first_down', models.SmallIntegerField()),
                ('third_down_att', models.SmallIntegerField()),
                ('third_down_conv', models.SmallIntegerField()),
                ('third_down_failed', models.SmallIntegerField()),
                ('timeout', models.SmallIntegerField()),
                ('xp_aborted', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'play',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gsis_name', models.CharField(blank=True, max_length=75, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.TextField()),
                ('profile_id', models.IntegerField(blank=True, null=True)),
                ('profile_url', models.CharField(blank=True, max_length=255, null=True)),
                ('uniform_number', models.SmallIntegerField(blank=True, null=True)),
                ('birthdate', models.CharField(blank=True, max_length=75, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.SmallIntegerField(blank=True, null=True)),
                ('weight', models.SmallIntegerField(blank=True, null=True)),
                ('years_pro', models.SmallIntegerField(blank=True, null=True)),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_id', models.SmallIntegerField()),
                ('play_id', models.SmallIntegerField()),
                ('defense_ast', models.SmallIntegerField()),
                ('defense_ffum', models.SmallIntegerField()),
                ('defense_fgblk', models.SmallIntegerField()),
                ('defense_frec', models.SmallIntegerField()),
                ('defense_frec_tds', models.SmallIntegerField()),
                ('defense_frec_yds', models.SmallIntegerField()),
                ('defense_int', models.SmallIntegerField()),
                ('defense_int_tds', models.SmallIntegerField()),
                ('defense_int_yds', models.SmallIntegerField()),
                ('defense_misc_tds', models.SmallIntegerField()),
                ('defense_misc_yds', models.SmallIntegerField()),
                ('defense_pass_def', models.SmallIntegerField()),
                ('defense_puntblk', models.SmallIntegerField()),
                ('defense_qbhit', models.SmallIntegerField()),
                ('defense_safe', models.SmallIntegerField()),
                ('defense_sk', models.FloatField()),
                ('defense_sk_yds', models.SmallIntegerField()),
                ('defense_tkl', models.SmallIntegerField()),
                ('defense_tkl_loss', models.SmallIntegerField()),
                ('defense_tkl_loss_yds', models.SmallIntegerField()),
                ('defense_tkl_primary', models.SmallIntegerField()),
                ('defense_xpblk', models.SmallIntegerField()),
                ('fumbles_forced', models.SmallIntegerField()),
                ('fumbles_lost', models.SmallIntegerField()),
                ('fumbles_notforced', models.SmallIntegerField()),
                ('fumbles_oob', models.SmallIntegerField()),
                ('fumbles_rec', models.SmallIntegerField()),
                ('fumbles_rec_tds', models.SmallIntegerField()),
                ('fumbles_rec_yds', models.SmallIntegerField()),
                ('fumbles_tot', models.SmallIntegerField()),
                ('kicking_all_yds', models.SmallIntegerField()),
                ('kicking_downed', models.SmallIntegerField()),
                ('kicking_fga', models.SmallIntegerField()),
                ('kicking_fgb', models.SmallIntegerField()),
                ('kicking_fgm', models.SmallIntegerField()),
                ('kicking_fgm_yds', models.SmallIntegerField()),
                ('kicking_fgmissed', models.SmallIntegerField()),
                ('kicking_fgmissed_yds', models.SmallIntegerField()),
                ('kicking_i20', models.SmallIntegerField()),
                ('kicking_rec', models.SmallIntegerField()),
                ('kicking_rec_tds', models.SmallIntegerField()),
                ('kicking_tot', models.SmallIntegerField()),
                ('kicking_touchback', models.SmallIntegerField()),
                ('kicking_xpa', models.SmallIntegerField()),
                ('kicking_xpb', models.SmallIntegerField()),
                ('kicking_xpmade', models.SmallIntegerField()),
                ('kicking_xpmissed', models.SmallIntegerField()),
                ('kicking_yds', models.SmallIntegerField()),
                ('kickret_fair', models.SmallIntegerField()),
                ('kickret_oob', models.SmallIntegerField()),
                ('kickret_ret', models.SmallIntegerField()),
                ('kickret_tds', models.SmallIntegerField()),
                ('kickret_touchback', models.SmallIntegerField()),
                ('kickret_yds', models.SmallIntegerField()),
                ('passing_att', models.SmallIntegerField()),
                ('passing_cmp', models.SmallIntegerField()),
                ('passing_cmp_air_yds', models.SmallIntegerField()),
                ('passing_incmp', models.SmallIntegerField()),
                ('passing_incmp_air_yds', models.SmallIntegerField()),
                ('passing_int', models.SmallIntegerField()),
                ('passing_sk', models.SmallIntegerField()),
                ('passing_sk_yds', models.SmallIntegerField()),
                ('passing_tds', models.SmallIntegerField()),
                ('passing_twopta', models.SmallIntegerField()),
                ('passing_twoptm', models.SmallIntegerField()),
                ('passing_twoptmissed', models.SmallIntegerField()),
                ('passing_yds', models.SmallIntegerField()),
                ('punting_blk', models.SmallIntegerField()),
                ('punting_i20', models.SmallIntegerField()),
                ('punting_tot', models.SmallIntegerField()),
                ('punting_touchback', models.SmallIntegerField()),
                ('punting_yds', models.SmallIntegerField()),
                ('puntret_downed', models.SmallIntegerField()),
                ('puntret_fair', models.SmallIntegerField()),
                ('puntret_oob', models.SmallIntegerField()),
                ('puntret_tds', models.SmallIntegerField()),
                ('puntret_tot', models.SmallIntegerField()),
                ('puntret_touchback', models.SmallIntegerField()),
                ('puntret_yds', models.SmallIntegerField()),
                ('receiving_rec', models.SmallIntegerField()),
                ('receiving_tar', models.SmallIntegerField()),
                ('receiving_tds', models.SmallIntegerField()),
                ('receiving_twopta', models.SmallIntegerField()),
                ('receiving_twoptm', models.SmallIntegerField()),
                ('receiving_twoptmissed', models.SmallIntegerField()),
                ('receiving_yac_yds', models.SmallIntegerField()),
                ('receiving_yds', models.SmallIntegerField()),
                ('rushing_att', models.SmallIntegerField()),
                ('rushing_loss', models.SmallIntegerField()),
                ('rushing_loss_yds', models.SmallIntegerField()),
                ('rushing_tds', models.SmallIntegerField()),
                ('rushing_twopta', models.SmallIntegerField()),
                ('rushing_twoptm', models.SmallIntegerField()),
                ('rushing_twoptmissed', models.SmallIntegerField()),
                ('rushing_yds', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'play_player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
    ]
