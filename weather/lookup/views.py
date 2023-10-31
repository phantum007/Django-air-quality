from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        urlss = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=E8603FBE-DBC5-442D-BD85-7869C7B507B7"
        try:
            api_request = requests.get(urlss)
            api_res = json.loads(api_request.content)
            api_res[0]["zipcode"]= zipcode
            return render(request,'home.html',{"api":api_res})
        except: 
            return render(request,'error.html',{})
        # return render(request, 'home.html', {'zipcode':zipcode})

    else:
        urlss = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10004&distance=25&API_KEY=E8603FBE-DBC5-442D-BD85-7869C7B507B7"
        try:
            api_request = requests.get(urlss)
            api_res = json.loads(api_request.content)
            return render(request,'home.html',{"api":api_res})
        except: 
            return render(request,'error.html',{})
 


def about(request):
    return render(request,'about.html',{})

def error(request):
    return render(request,'error.html',{})