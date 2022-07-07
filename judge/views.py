from http.client import HTTPException, HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from judge.models import Problem


"""
FILE STRUCTURE
(Django looks for templates/static files for an app in a
directory having it's name as the app's name inside
a templates directory inside the app itself)
--judge (app directory)
---templates (templates directory)
----judge (another subdirectory whose name is same as app)
-----<static files> (templates/static files)
"""


def get_problems(request):
    problem_list= Problem.objects.order_by('-level')
    context_to_template={'problem_list':problem_list} 
    return render(request, 'judge/problems.html', context_to_template)

def get_user_data(request):
    return render(request, 'judge/user_data.html')

def submit_solution(request, prob_id):
    return render(request, 'judge/submit.html')
