import random
import sys

import datetime
from django.core.management.base import BaseCommand
from django.db import models

from contestdata.models import Candidate, Activities, Mentor, Activity_mentor


class Command(BaseCommand):
    args = 'team ID'
    help = 'our help string comes here'

    def usage(self):
        print('Error: Verify your command arguments')
        print('Usage: createactivityscore [song name] [mentor name] [score]')

    def validateArgs(self, argv):

        argsCount = len(argv)
        if argsCount <= 4:
            self.usage()
            sys.exit(1)

    def create_activity_score(self):
        self.validateArgs(sys.argv)
        songName = sys.argv[2]
        mentorName = sys.argv[3]
        mentorScore = sys.argv[4]
        mentor = Mentor.objects.filter(name=mentorName)

        if not mentor:
            print('Mentor does not exist, run creatementor to add it')
            sys.exit(1)
        activity = Activities.objects.filter(song_name=songName)
        if (not activity):
            print('Activity does not exist, run createactivity to add it')
            sys.exit(1)
        else:
            mentor_activity = Activity_mentor(mentor_id=mentor[0],
                                              activity_id=activity[0],
                                              mentor_score=mentorScore)
            mentor_activity.save()
            updatedScore = Activity_mentor.objects.filter(activity_id=activity[0].id).aggregate(models.Avg('mentor_score'))['mentor_score__avg']
            activity[0].activity_score = updatedScore
            activity[0].save()
            candidate = Candidate.objects.get(pk=activity[0].candidate_id)
            candidate.average_score = Activities.objects.filter(candidate_id=candidate.id).aggregate(models.Avg('activity_score'))['activity_score__avg']
            candidate.save()

        print('Activity rated: %s' % activity)

    def handle(self, *args, **options):
        self.create_activity_score()