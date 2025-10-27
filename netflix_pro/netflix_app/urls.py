from django.urls import path
from . import views
urlpatterns=[
    path('kantara/',view=views.kantara),
    path('bahubali/',view=views.bahubali),
    path('pushpa/',view=views.pushpa),
]