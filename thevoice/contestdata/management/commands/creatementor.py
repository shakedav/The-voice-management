import random
import sys

from django.core.management.base import BaseCommand
from contestdata.models import Mentor_Team, Mentor, Team, Member


class Command(BaseCommand):
    args = 'team ID'
    help = 'our help string comes here'

    def usage(self):
        print('Error: Verify your command arguments')
        print('Usage: creatementor [mentor name] [team name]')

    def validateArgs(self, argv):

        argsCount = len(argv)
        if argsCount <= 3:
            self.usage()
            sys.exit(1)

    def create_mentor(self):
        self.validateArgs(sys.argv)
        mentorName = sys.argv[2]
        teamName = sys.argv[3]

        team = Team.objects.filter(name=teamName)
        print(team)
        if not team:
            team = Team(name=teamName)
            team.save()
            mentor = Mentor(name=mentorName)

            if not (Mentor.objects.filter(name=mentorName)):
                mentor.save()
            else:
                print('mentor exists: %s' % mentor)
                sys.exit(1)
        else:
            print('Team already exists: teamID: %s teamName: %s' % (team[0].id, team[0].name))
            sys.exit(1)
        ct = Mentor_Team(mentor_id=mentor, team_id=team)
        ct.save()
        member = Member(user_name=mentorName, password='1234', user_type='Mentor')
        member.save()
        print('mentor created: %s' % mentor)
        print('login user details for mentor are: username: %s, password: 1234' % mentorName)

    def handle(self, *args, **options):
        self.create_mentor()