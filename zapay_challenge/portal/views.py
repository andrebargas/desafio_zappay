from django.shortcuts import render
import requests
import json

def index(request):
    a = requests.get('https://api.spacexdata.com/v3/launches/next')
    data = a.text
    print( "DATA \n")
    print(data)
    # print( "DATA 2 \n")
    # print(data[4])
    jsondata = a.json()
    print( "JSON DATA \n")
    print(jsondata['flight_number'])
    # loaded_data = a.json()
    # print(loaded_data['flight_number'])
    return render(request, 'index.html')
