from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeIndex),
    path('header', views.header),
    path('game/<int:gameID/dayPhase', views.dayPhase),
    path('game/<int:gameID>/nightPhase', views.nightPhase),
    path('host', views.createGame),
    path('game/<int:gameID>', views.game),
    path('game/<int:gameID>/join', views.joinGame),
    path('game/<int:gameID>/update', views.updateGame),
    path('game/<int:gameID>/start', views.startGame),
    path('game/<int:gameID>/kick/<int:playerID>', views.kickPlayer),
    path('game/<int:gameID>/calcPhaseNight', views.calcPhaseNight),
    
    path('game/<int:gameID>/delete', views.deleteGame),
    path('fakeUserGen', views.fakeUsers), # comment this for production -- generate fake users for debug
    path('game/<int:gameID>/addFakeUsers', views.addFakeUsers), # comment this for production -- add fake users to game

]
