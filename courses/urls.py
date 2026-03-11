from django.urls import path
from .views import (
    CourseDetailView,
    CourseListView,
    # my_fbv
)

app_name = "courses"

urlpatterns = [
    path('',CourseListView.as_view(), name="courses-list"),
    path('<int:id>/', CourseDetailView.as_view(), name="courses-list"),
    # path('',CourseDetailView.as_view(template_name="contact.html"), name="courses-list"),
    # path('',CourseDetailView.as_view(template_name="contact.html"), name="courses-list"),
    # path('',my_fbv, name="courses-list")
]