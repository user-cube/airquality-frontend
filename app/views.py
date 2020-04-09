from django.http import Http404
from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    r = requests.get("https://tqsspring.herokuapp.com/cities/")
    tparams = {
        'cities' : r.json()
    }
    return render(request, 'home.html', tparams)

def airquality(request, city):
    r = requests.get("https://tqsspring.herokuapp.com/airquality/"+ city)
    if r.status_code != 200:
        raise Http404
    dic = r.json()
    tparams = {
        'city' : city,
        'status' : dic["data"]["indexes"]["prt_qualar"]["category"],
        'dominant': dic["data"]["indexes"]["prt_qualar"]["dominant_pollutant"],
        'no2' : str(dic["data"]["pollutants"]["no2"]["concentration"]["value"]) + " " +
                dic["data"]["pollutants"]["no2"]["concentration"]["units"],
        'o3': str(dic["data"]["pollutants"]["o3"]["concentration"]["value"]) + " " +
               dic["data"]["pollutants"]["o3"]["concentration"]["units"],
        'pm25': str(dic["data"]["pollutants"]["pm25"]["concentration"]["value"]) + " " +
               dic["data"]["pollutants"]["pm25"]["concentration"]["units"],
        'so2': str(dic["data"]["pollutants"]["so2"]["concentration"]["value"]) + " " +
                dic["data"]["pollutants"]["so2"]["concentration"]["units"],
        'pm10': str(dic["data"]["pollutants"]["pm10"]["concentration"]["value"]) + " " +
                dic["data"]["pollutants"]["pm10"]["concentration"]["units"],
        'co': str(dic["data"]["pollutants"]["co"]["concentration"]["value"]) + " " +
                dic["data"]["pollutants"]["co"]["concentration"]["units"],
    }
    return render(request, 'airquality.html', tparams)

def forecast(request, city):
    r = requests.get("https://tqsspring.herokuapp.com/forecast/" + city)
    if r.status_code != 200:
        raise Http404
    dic = r.json()
    tparams = {
        'city': city,
            'day1Date': dic["data"][1]["forecastDate"],
        'day1TMax': dic["data"][0]["tMax"],
        'day1TMin': dic["data"][0]["tMin"],
        'day1TPreProb': dic["data"][0]["precipitaProb"],
        'day1WindDir': dic["data"][0]["predWindDir"],
        'day1WindSpeed': dic["data"][0]["classWindSpeed"],
        'day2Date': dic["data"][1]["forecastDate"],
        'day2TMax': dic["data"][1]["tMax"],
        'day2TMin': dic["data"][1]["tMin"],
        'day2TPreProb': dic["data"][1]["precipitaProb"],
        'day2WindDir': dic["data"][1]["predWindDir"],
        'day2WindSpeed': dic["data"][1]["classWindSpeed"],
        'day3Date': dic["data"][2]["forecastDate"],
        'day3TMax': dic["data"][2]["tMax"],
        'day3TMin': dic["data"][2]["tMin"],
        'day3TPreProb': dic["data"][2]["precipitaProb"],
        'day3WindDir': dic["data"][2]["predWindDir"],
        'day3WindSpeed': dic["data"][2]["classWindSpeed"],
        'day4Date': dic["data"][3]["forecastDate"],
        'day4TMax': dic["data"][3]["tMax"],
        'day4TMin': dic["data"][3]["tMin"],
        'day4TPreProb': dic["data"][3]["precipitaProb"],
        'day4WindDir': dic["data"][3]["predWindDir"],
        'day4WindSpeed': dic["data"][3]["classWindSpeed"],
        'day5Date': dic["data"][4]["forecastDate"],
        'day5TMax': dic["data"][4]["tMax"],
        'day5TMin': dic["data"][4]["tMin"],
        'day5TPreProb': dic["data"][4]["precipitaProb"],
        'day5WindDir': dic["data"][4]["predWindDir"],
        'day5WindSpeed': dic["data"][4]["classWindSpeed"],
    }
    return render(request, 'forecast.html', tparams)

def coordinates(request, city):
    r = requests.get("https://tqsspring.herokuapp.com/coordinates/" + city)
    if r.status_code != 200:
        raise Http404
    dic = r.json()
    tparams = {
        'city': city,
        'latitude' : dic["latitude"],
        'longitude' : dic["longitude"]
    }
    return render(request, 'coordinates.html', tparams)