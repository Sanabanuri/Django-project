from django.urls import path
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("courses/", views.course_list, name="course_list"),
]