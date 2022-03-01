import requests
city = "Moscow, RU"
appid = "7d76b9051b5a3e30909bb5bf560e7e47"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("____________________________")
print("Погода на сегодня:")
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:",  data['main']['temp'], "C"+chr(176))
print("Минимальная температура:", data['main']['temp_min'], "C"+chr(176))
print("Максимальная температура:", data['main']['temp_max'], "C"+chr(176))
print("Скорость ветра:", data['wind']['speed'], "м/с")
print("Видимость:", data['visibility'], "м")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("____________________________")
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
          '{0:+3.0f}'.format(i['main']['temp']), "C"+chr(176), "> \r\nПогодные условия <",
          i['weather'][0]['description'], ">", "\r\nСкорость ветра <", i['wind']['speed'], "м/с >",
          "\r\nВидимость <", i['visibility'], "м >")
    print("____________________________")