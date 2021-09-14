
from django.shortcuts import render
import requests
from django.http import HttpResponse
import json

def EmployeeListView(request):
    response = requests.get('http://127.0.0.1:1400/api/employees/')

    if response.status_code==200:
        try:
            dict_data = json.loads(response.text)
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
        else:
            return HttpResponse(dict_data)
    else:
        print(response.status_code)
        return HttpResponse(response.text)



def EmployeeDetailView(request,pk):
    response = requests.get('http://127.0.0.1:1400/api/employees/'+str(pk)+'/')

    if response.status_code==200:
        try:
            return HttpResponse(response,content_type='application/json')
            # dict_data = json.loads(response)
        except ValueError:
            return HttpResponse('Sorry, You are not getting JSON Response')
        # else:
        #     return HttpResponse(dict_data)
    else:
        print(response.status_code)
        return HttpResponse(response.text)


