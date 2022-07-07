from django.urls import path

from . import views

urlpatterns = [
    path('problems/', views.get_problems),                   #this will lead to problems' list
    path('user_data/', views.get_user_data),                 #this will lead to users's handle   
    path('submit/<int:prob_id>', views.submit_solution),     #this will lead to submit page
                                                #<int:prob_id> will be taken as an argument to submit_solution()
]