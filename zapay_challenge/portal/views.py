from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'index.html')

def next_launches(request):
    data = requests.get('https://api.spacexdata.com/v3/launches/upcoming')
    json_data = data.json()
    return render(request, 'upcoming.html', {'data': json_data})

def next_launch(request):
    try:
        data = requests.get('https://api.spacexdata.com/v3/launches/next')
        json_data = data.json()
    except requests.exceptions.ConnectionError as e:
        print("No response")
        return render(request, 'next.html') 
    return render(request, 'next.html', {'data': json_data})

def last_launch(request):
    data = requests.get('https://api.spacexdata.com/v3/launches/latest')
    json_data = data.json()
    return render(request, 'last.html', {'data': json_data})

def past_launches(request):
    data = requests.get('https://api.spacexdata.com/v3/launches/past')
    json_data = data.json()
    return render(request, 'past.html', {'data': json_data})
