# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "447a6113f0msha8745ad2d7abc97p10f73ajsn36929ee3f8cc",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)

# Create your views here.
def helloworldview(request):
    noofresults=int(response['results'])
    mylist=[]
    for i in range(0,noofresults):
        mylist.append(response['response'][i]['country'])
    mylist=sorted(mylist)
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        noofresults=int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'total':total,'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths}
        return render(request,'index.html',context)
    
    context={'mylist':mylist}
    return render(request,'index.html',context)
    