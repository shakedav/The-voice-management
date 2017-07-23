import random
import sys

import datetime
from django.core.management.base import BaseCommand
from contestdata.models import Candidate, Activities


class Command(BaseCommand):
    args = 'team ID'
    help = 'our help string comes here'

    def usage(self):
        print('Error: Verify your command arguments')
        print('Usage: createactivity [song name] [candidate name] [date(YYYY-MM-DD] [score]')

    def validateArgs(self, argv):

        argsCount = len(argv)
        if argsCount <= 5:
            self.usage()
            sys.exit(1)

    def create_activity(self):
        self.validateArgs(sys.argv)
        songName = sys.argv[2]
        candidateName = sys.argv[3]
        activityDate = datetime.datetime.strptime(sys.argv[4], "%Y-%m-%d").date()
        activityScore = sys.argv[5]
        candidate = Candidate.objects.filter(candidate_name=candidateName)
        print(candidate)
        if not candidate:
            print('Candidate does not exist, run createcandidate to add it')
            sys.exit(1)
        else:
            activity = Activities(song_name=songName,
                                  candidate=candidate[0],
                                  date_performed=activityDate,
                                  activity_score=activityScore)
            activity.save()
        print('Activity created: %s' % activity)

    def handle(self, *args, **options):
        self.create_activity()