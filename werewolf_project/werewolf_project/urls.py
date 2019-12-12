from django.urls import path, include

urlpatterns = [
    path('', include('login_app.urls')),
    path('/home/', include('werewolf_app.urls')),
]
