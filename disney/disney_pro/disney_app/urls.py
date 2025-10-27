from django.urls import path
from . import views
urlpatterns=[
    path("marvel/",view=views.marvel),
    path("dc/",view=views.dc),
    path("users/<int:id>",view=views.users_data),
    path("register/",view=views.register),
    path("registration/",view=views.registeration)
]