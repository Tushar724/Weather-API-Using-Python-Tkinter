city_name="Bhopal"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=97ea69deadc2006e476c84a514d815b6").json()
print(data)