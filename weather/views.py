import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    app_id = "7b06996e671b504dcc4a6e2ed52111ed"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id
    city = "London"

    response = requests.get(url.format(city)).json()
    # print(response.text)

    city_info = {
        'city': city,
        'temp': response['main']['temp'],
        'feels_like': response['main']['feels_like'],
        'clouds': response['clouds']['all'],
        'icon': response['weather']['icon']
    }

    context = {'info': city_info)}

    return render(request, 'weather/index.html', context)
