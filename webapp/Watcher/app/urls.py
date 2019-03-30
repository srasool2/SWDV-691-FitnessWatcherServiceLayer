from django.urls import path
from .views import ListBlogsView, WorkoutList

urlpatterns = [
    path('blogs', ListBlogsView.as_view(), name="blogs_all"),
    path('workouts', WorkoutList.as_view(), name="workout_all"),
]
