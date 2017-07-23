import json

from django.db import models
from django.http import HttpResponse

from .models import Candidate, Activities, Mentor_Team, Mentor, Team, Candidate_team, Member


def teamCandidates(request, team_id):
    result = []
    data = Candidate_team.objects.select_related('candidate_id', 'team_id').filter(team_id=team_id)
    for candidate in data:
        averageScore, teamAverageScore = getAverages(candidate.team_id.id, candidate.candidate_id.id)
        json_obj = {
            'candidateID': candidate.candidate_id.id,
            'candidateName': candidate.candidate_id.candidate_name,
            'averageScore': averageScore,
            'teamAverageScore': teamAverageScore,
            'teamName': candidate.team_id.name,
            'teamID': candidate.team_id.id
        }
        result.append(json_obj)

    return HttpResponse(json.dumps(result), content_type="application/json")

def candidates(request, candidate_name=None):
    result=[]
    if not candidate_name:
        data = Candidate.objects.select_related('team')
        for candidate in data:
            averageScore, teamAverageScore = getAverages(candidate.team.id, candidate.id)

            json_obj = {
                'candidateID': candidate.pk,
                'candidateName': candidate.candidate_name,
                'teamName': candidate.team.name,
                'teamID': candidate.team.id,
                'averageScore': candidate.average_score,
                'teamAverageScore': teamAverageScore
            }
            result.append(json_obj)
    else:
        data = Candidate.objects.select_related('team').filter(candidate_name=candidate_name)
        averageScore, teamAverageScore = getAverages(data[0].team.id, data[0].candidate.id)
        for candidate in data:
            json_obj = {
                'candidateID': candidate.pk,
                'candidateName': candidate.candidate_name,
                'averageScore': candidate.average_score,
                'teamName': candidate.team.name,
                'teamID': candidate.team.id,
                'teamAverageScore': teamAverageScore
            }
            result.append(json_obj)

    return HttpResponse(json.dumps(result), content_type="application/json")

def getAverages(teamID, candidateID):
    candidatesIDS = list(Candidate_team.objects.filter(team_id=teamID).all().values_list('candidate_id'))
    teamAverageScore = Activities.objects.filter(candidate_id__in=candidatesIDS).aggregate(models.Avg('activity_score'))['activity_score__avg']
    averageScore = Activities.objects.filter(candidate_id=candidateID).aggregate(models.Avg('activity_score'))['activity_score__avg']
    return averageScore , teamAverageScore


def activities(request, candidate_id=None):
    result=[]
    if not candidate_id:
        activityData = Activities.objects.select_related('candidate')

        for activity in activityData:
            json_obj = {
                'songName': activity.song_name,
                'activityAvgScore': activity.activity_score,
                'candidateName': activity.candidate.candidate_name,
                'datePerformed': str(activity.date_performed),
                'activityID': activity.pk
            }
            result.append(json_obj)
    else:
        activityData = Activities.objects.select_related('candidate').filter(candidate=candidate_id)

        for activity in activityData:
            json_obj = {
                'songName': activity.song_name,
                'activityAvgScore': activity.activity_score,
                'candidateName': activity.candidate.candidate_name,
                'datePerformed': str(activity.date_performed),
                'activityID': activity.pk
            }
            result.append(json_obj)

    return HttpResponse(json.dumps(result), content_type="application/json")

def teams(request, mentor_id=None):
    result = []
    if not mentor_id:
        data = Mentor_Team.objects.select_related('mentor_id', 'team_id')
        for team in data:
            json_obj = {
                'name': team.team_id.name,
                'teamID': team.team_id.pk,
                'mentorName': team.mentor_id.name,
                'mentorID': team.mentor_id.id,
                'isVisible': True
            }
            result.append(json_obj)
    else:
        data = Mentor_Team.objects.select_related('mentor_id', 'team_id').filter(mentor_id=(Mentor.objects.filter(id=mentor_id).all()[0]))
        for team in data:
            json_obj = {
                'name': team.team_id.name,
                'teamID': team.team_id.pk,
                'mentorName': team.mentor_id.name,
                'mentorID': team.mentor_id.id,
                'isVisible': True
            }
            result.append(json_obj)

    return HttpResponse(json.dumps(result), content_type="application/json")

def login(request):
    userDetails = json.loads(request.body)
    print(userDetails)
    userName = userDetails['username']
    password = userDetails['password']
    existingUser = Member.objects.filter(user_name=userName).all()
    if len(existingUser) == 0:
        return HttpResponse(json.dumps({'error': 'user does not exist'}), content_type="application/json", status=404)
    else:
        if (password == existingUser[0].password):
            print('correct')
            print (existingUser[0])
            if existingUser[0]:
                mentor = Mentor.objects.filter(name=userName)
                if len(mentor) > 0:
                    mentorID = mentor[0].id
                else:
                    mentorID = None
            else:
                mentorID = None
            json_obj ={
                'userType':existingUser[0].user_type,
                'mentorId': mentorID
            }
            return HttpResponse(json.dumps([json_obj]), content_type="application/json")
        return HttpResponse(json.dumps({'error': 'incorrect password or username'}), content_type="application/json", status=401)