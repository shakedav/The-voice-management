from django.conf.urls import url
from django.contrib.auth.views import login
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'candidates/$', views.candidates, name='candidates'),
    url(r'candidates/(?P<candidate_name>[\w|\W]+)/$', views.candidates, name='candidates'),
    url(r'activities/$', views.activities, name='activities'),
    url(r'activities/(?P<candidate_id>[0-9]+)/$', views.activities, name='activities'),
    url(r'^mentors/(?P<mentor_id>[0-9]+)/teams/$', views.teams, name='mentor-teams'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/(?P<team_id>[0-9]+)/Candidates/$', views.teamCandidates, name='teams'),
    url(r'^login/$', views.login , name='login'),
]

