from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    urls = "http://api.openweathermap.org/data/2.5/forecast?id=524901&&units=metric&appid=b08cffa8c9cda911c865dd3b9e122486"
    # city = "Haridwar"
    
    if request.method =="POST":
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []
    
    for city in cities:        
        r= requests.get(urls.format(city)).json()
        
        city_weather = {
                "city": city,
                "temperature": r["list"][0]['main']['temp'],
                "description":r['list'][0]['weather'][0]['description'],
                "icon": r['list'][0]['weather'][0]['icon']
            }
        
        weather_data.append(city_weather)
        
    print(weather_data)

    context = {'city_weather ':city_weather,'form':form}
    return render(request,"weather/weather.html",context)

