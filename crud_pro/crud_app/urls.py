from django.urls import path
from . import views
urlpatterns=[
    path("greetings/",view=views.greetings),
    path('first/',view=views.template),
    path('faculty/<int:id>',view=views.faculty_data),
    path('faculty/',view=views.faculty_data),
    path('register/',view=views.register),
    path('update_faculty/<int:id>',view=views.update_faculty),
    path('fac_update/<int:id>',view=views.fac_update),
    path('delete_fac/<int:id>',view=views.delete_faculty),
    path('faculty_form/',view=views.faculty_form),
    path('upd_fac/<int:id>',view=views.upd_faculty)
]