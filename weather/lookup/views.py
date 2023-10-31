from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    urlss = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10004&distance=25&API_KEY=E8603FBE-DBC5-442D-BD85-7869C7B507B7"
    try:
        api_request = requests.get(urlss)
        print("api_request", api_request.content)

        api_res = json.loads(api_request.content)
        print("api_res",api_res)
        return render(request,'home.html',{"api":api_res})
    except: 
        return render(request,'error.html',{})
 


def about(request):
    return render(request,'about.html',{})

def error(request):
    return render(request,'error.html',{})