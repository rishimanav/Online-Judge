from http.client import HTTPException, HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse


def problems(request):
    return HttpResponse("problems page")

def account(request):
    return HttpResponse("your account details")

def submit(request):
    return HttpResponse("submit code page")

