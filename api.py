import request

api_key = "d6eadc22b196c4f48c9ac3d7f8647869"
url = "https://api.openweathermap.org/data/2.5/weather"

city = input("sisesya linn")

params = {
    "appid:" api_key,
    }

request.get(url,city)