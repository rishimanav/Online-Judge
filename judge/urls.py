from django.urls import path

from . import views

urlpatterns = [
    path('problems/', views.problems),  #this will lead to problems' list
    path('account/', views.account),    #this will lead to users's handle   
    path('submit/', views.submit),      #this will lead to submit page
]