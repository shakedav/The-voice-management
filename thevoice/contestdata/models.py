import datetime


from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible

class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Team'

class Mentor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Mentor'

class Mentor_Team(models.Model):

    team_id = models.OneToOneField(Team, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.team_id.name, self.mentor_id.name)

    class Meta:
        db_table = 'MentorTeam'

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=200, unique=True   )
    average_score = models.FloatField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate_name

    class Meta:
        db_table = 'Candidate'

class Candidate_team(models.Model):
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.candidate_id.candidate_name, self.team_id.name)

    class Meta:
        db_table = 'CandidateTeam'

class Activities(models.Model):
    song_name = models.CharField(max_length=200)
    activity_score = models.FloatField(default=0)
    date_performed = models.DateField(default=timezone.now)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.song_name, self.candidate.candidate_name)

    class Meta:
        db_table = 'Activities'

class Activity_mentor(models.Model):
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentor_score = models.FloatField(default=0)

    def __str__(self):
        return "%s %s" % (self.activity_id, self.mentor_id)

    class Meta:
        db_table = 'ActivityMentor'

class Member(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=64)
    user_type = models.CharField(max_length=200)

    class Meta:
        db_table = 'Member'
