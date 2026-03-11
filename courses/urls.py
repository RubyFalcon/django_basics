from django.urls import path
from .views import (
    CourseDetailView,
    # my_fbv
)

app_name = "courses"

urlpatterns = [
    path('',CourseDetailView.as_view(), name="courses-list"),
    # path('',my_fbv, name="courses-list")
]