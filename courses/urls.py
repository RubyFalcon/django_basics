from django.urls import path
from .views import (
    CourseDetailView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView
    # my_fbv
)

app_name = "courses"

urlpatterns = [
    path('create/',CourseCreateView.as_view(), name="courses-create"),
    path('',CourseListView.as_view(), name="courses-list"),
    path('<int:id>/', CourseDetailView.as_view(), name="courses-list"),
    path('<int:id>/update/',CourseUpdateView.as_view(), name="courses-update"),
    # path('',my_fbv, name="courses-list")
]