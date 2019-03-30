from rest_framework import serializers
from .models import Blogs, WorkoutPlan


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ("blog_id", "blog_link", "blog_summary", "blog_title")

class WPSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ("workout_id", "workout_name", "workout_duration")