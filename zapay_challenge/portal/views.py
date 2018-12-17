from django.shortcuts import render
from django import http
import requests
import json

def index(request):
    return render(request, 'index.html')

def next_launches(request):
    try:
        data = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
        json_data = data.json()
    except requests.exceptions.ConnectionError as e:
        print("No response")
        return render(request, 'next.html', status='502')
    print(json_data)
    return render(request, 'upcoming.html', {'data': json_data}, status='200')

def next_launch(request):
    try:
        data = requests.get('https://api.spacexdata.com/v3/launches/next')
        json_data = data.json()
    except requests.exceptions.ConnectionError as e:
        print("No response")
        return render(request, 'next.html', status='502')
    return render(request, 'next.html', {'data': json_data}, status='200')

def last_launch(request):
    try:
        data = requests.get('https://api.spacexdata.com/v3/launches/latest')
        json_data = data.json()
    except requests.exceptions.ConnectionError as e:
        print("No response")
        return render(request, 'next.html', status='502')
    return render(request, 'last.html', {'data': json_data}, status='200')


def past_launches(request):
    try:
        data = requests.get('https://api.spacexdata.com/v3/launches/past')
        json_data = data.json()
    except requests.exceptions.ConnectionError as e:
        print("No response")
        return render(request, 'next.html', status='502')
    return render(request, 'past.html', {'data': json_data}, status='200')
