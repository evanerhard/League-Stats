from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register', views.register, name='register'),

    url(r'^drives/$', views.drives_list, name='drives_list'),
    url(r'^drives/(?P<drive_id>[a-zA-z--9]+)$', views.drive_view, name='drives'),

    url(r'^players/$', views.players_list, name='players_list'),
    url(r'^players/(?P<player_id>[a-zA-Z--9]+)$', views.player_view, name='players'),
    url(r'^passing/(?P<player_id>[a-zA-Z--9]+)$', views.passing_yds_player),


    url(r'^games/$', views.games_list, name='games_list'),
    url(r'^games/(?P<gsis_id>[a-zA-z--9]+)$', views.game_view, name='games'),

    url(r'^teams/$', views.teams_list, name='teams_list'),
    url(r'^teams/(?P<team_id>[a-zA-z--9]+)$', views.team_view, name='teams'),

    url(r'^top/$', views.five_qb_list, name='top'),

    url(r'^chart_example/$', views.chart_example, name='chart_example'),
]
