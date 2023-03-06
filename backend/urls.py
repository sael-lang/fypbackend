from django.contrib import admin
from django.urls import path
from fypapp.views import *

urlpatterns = [
    path('', postdata.as_view()),
    path('signin',SIGNIN.as_view()),
    path('savedepi',savedirectorEPI.as_view()),
    path('showdepi',showdirectorEPI.as_view()),
    path('countdepi',countdirectorEPI.as_view()),
    path('savehosp',savehospital.as_view()),
    path('showhosp',showhospital.as_view()),
    path('counthosp',counthospital.as_view()),
    path('savemsi',savemedicalSuperIntendent.as_view()),
    path('showmsi',showmedicalSuperIntendent.as_view()),
    path('countmsi',countmedicalSuperIntendent.as_view()),
    path('savevac',savevaccine.as_view()),
    path('showvac',showvaccine.as_view()),
    path('countvac',countvaccine.as_view()),
    path('savechild',savechild.as_view()),
    path('showchild',showchild.as_view()),
    path('countchild',countchild.as_view()),
    path('savehcw',savehealthcareworker.as_view()),
    path('showhcw',showhealthcareworker.as_view()),
    path('counthcw',counthealthcareworker.as_view()),
    path('saveasignv',saveassignedvaccine.as_view()),
    path('showasignv',showassignedvaccine.as_view()),
    path('countasignv',countassignedvaccine.as_view()),
    path('savevacr',savevaccineRecord.as_view()),
    path('showvacr',showvaccineRecord.as_view()),
    path('countvacr',countvaccineRecord.as_view()),
    path('updatevacr',updatevaccineRecord.as_view()),
    path('deletevacr',deletevaccineRecord.as_view()),
]
