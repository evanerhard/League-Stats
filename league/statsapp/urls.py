from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register', views.register, name='register'),
    url(r'top', views.five_qb_list, name='top'),
    url(r'players', views.players_list, name='players_list'),
    

]
