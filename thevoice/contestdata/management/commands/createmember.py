import random
import sys

import datetime
from django.core.management.base import BaseCommand
from contestdata.models import Candidate, Activities, Member


class Command(BaseCommand):
    args = 'team ID'
    help = 'our help string comes here'

    def usage(self):
        print('Error: Verify your command arguments')
        print('Usage: createmembr [member name] [password] [Mentor / Admin]')

    def validateArgs(self, argv):

        argsCount = len(argv)
        if argsCount <= 4:
            self.usage()
            sys.exit(1)

    def create_member(self):
        self.validateArgs(sys.argv)
        memberName = sys.argv[2]
        password = sys.argv[3]
        userType = sys.argv[4]
        member = Member(user_name=memberName, password=password, user_type=userType)
        member.save()
        print('member created: %s' % member)
        print('login user details for mentor are: username: %s, password: %s user is of type %s' % (memberName, password, userType))

    def handle(self, *args, **options):
        self.create_member()