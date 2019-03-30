from django.contrib import admin
from .models import Profile, WorkoutPlan, WorkoutPlanDetails, Blogs, ExerciseTrack

admin.site.register(ExerciseTrack)
admin.site.register(Blogs)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanDetails)

