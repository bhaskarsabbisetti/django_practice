from django.urls import path
from . import views
urlpatterns=[
    path('biryani/',view=views.biryani),
    path('noodiles/',view=views.noodiles)
]