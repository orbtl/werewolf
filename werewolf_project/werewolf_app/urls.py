from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeIndex),
    path('header', views.header),
    path('host', views.createGame),
    path('game/<int:gameID>', views.game),
]
