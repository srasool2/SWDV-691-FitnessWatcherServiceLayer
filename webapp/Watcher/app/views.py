from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Blogs, WorkoutPlan, WorkoutPlanDetails, ExerciseTrack
from .serializers import BlogsSerializer, WPSerializer
# Create your views here.

class ListBlogsView(generics.ListAPIView):
    """
    Get all blogs in the database.
    """
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class WorkoutList(APIView):
    """
    List all workouts with the exercises
    """
    def get(self,request,format=None, version=None):
        final_workout_data = []
        workouts = WorkoutPlan.objects.all()
        for workout_ in workouts:
            temp_ = {}
            temp_['workout_id'] = workout_.workout_id
            temp_['workout_name'] = workout_.workout_name
            temp_['workout_duration'] = workout_.workout_duration
            temp_['exercises'] = []
            workout_related_details = workout_.workoutplandetails_set.all()
            for workout_related_detail in workout_related_details:
                temp2_ = {}
                temp2_['name'] = workout_related_detail.exercise_id.exercise_name
                temp2_['num_sets'] = workout_related_detail.num_sets
                temp_['exercises'].append(temp2_)
            final_workout_data.append(temp_)
        
        return Response(final_workout_data)

