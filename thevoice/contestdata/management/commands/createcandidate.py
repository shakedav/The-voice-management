import random
import sys

from django.core.management.base import BaseCommand
from contestdata.models import Candidate, Candidate_team, Team


class Command(BaseCommand):
    args = 'team ID'
    help = 'our help string comes here'

    def usage(self):
        print('Error: Verify your command arguments')
        print('Usage: createcandidate [candidate name] [team name]')

    def validateArgs(self, argv):

        argsCount = len(argv)
        if argsCount <= 3:
            self.usage()
            sys.exit(1)

    def verify_candidate(self, candidateName,team):
        existingCandidate = Candidate.objects.filter(candidate_name=candidateName)
        if not existingCandidate:
            candidate = Candidate(candidate_name=candidateName, average_score=0.0, team_id=team.id)
            candidate.save()
        else:
            print('candidate exists and part of team %s' % existingCandidate[0].team.name)
            sys.exit(1)
        ct = Candidate_team(candidate_id=candidate, team_id=team)
        ct.save()
        print('candidate created: %s' % candidate)

    def create_candidate(self):
        self.validateArgs(sys.argv)
        if not sys.argv[2]:
            candidateName='candidate-'+ ''.join(random.choice('thevoice') for _ in range(8))
        else:
            candidateName = sys.argv[2]

        teamName = sys.argv[3]
        team = Team.objects.filter(name=teamName)
        if not team:
            team = Team(name=teamName)
            team.save()
            self.verify_candidate(candidateName, team)
        else:
            print(team)
            self.verify_candidate(candidateName, team[0])

    def handle(self, *args, **options):
        self.create_candidate()

