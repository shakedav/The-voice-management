from django.contrib import admin

from .models import *

admin.site.register(Candidate)
admin.site.register(Activities)
admin.site.register(Mentor)
admin.site.register(Team)
admin.site.register(Mentor_Team)
admin.site.register(Activity_mentor)
admin.site.register(Candidate_team)
