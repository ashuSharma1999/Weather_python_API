from django.shortcuts import render
import datetime 
import requests 

# Create your views here.
def home(request):
    t=datetime.datetime.now()
    d=t.strftime(' %a')
    x=str(d)+" "+str(t)
    city=request.GET.get("city","delhi")
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=389b0c0a4197346944451f8636944f62'
    data=requests.get(url).json()
    payload={
    'weather':data['weather'][0]['main'],
    'city':data['name'],
    'icon':data['weather'][0]['icon'],
    'kelvin_tempreture':data['main']['temp'],
    'celcius_tempreture':int(data['main']['temp']-273),
    'pressure':data['main']['pressure'],
    'humidity':data['main']['humidity'],
    'description':data['weather'][0]['description']
    }
    # context={'data':payload}
    # print(context)
    # return render(request,'home.html',context)
    return render(request,'home.html',{'data':payload,'date':x})
   