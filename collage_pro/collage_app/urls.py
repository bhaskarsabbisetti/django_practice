from django.urls import path
from . import views
urlpatterns=[
    path("greetings/",view=views.greetings),
    path("register/",view=views.register),
    path("student_data/",view=views.student_data),
    path("student_data/<int:id>",view=views.stu_data)
]