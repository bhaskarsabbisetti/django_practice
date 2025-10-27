from django.urls import path
from . import views

urlpatterns=[
    path("manchuria/",view=views.manchuria),
    path("biryani/",view=views.biryani),
]