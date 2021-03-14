import tkinter as tk
import requests
from datetime import datetime

def getWeather(canvas):
    # get your personal api from https://openweathermap.org
    city = textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e990a341618c60691023c3e9f9d869c7"
    try:
        # decode json by https://jsoneditoronline.org
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        temp_min = int(json_data['main']['temp_min'] - 273.15)
        temp_max = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']

        wind_speed = json_data['wind']['speed']
        
        r = datetime.fromtimestamp(json_data['sys']['sunrise']-28800)
        s = datetime.fromtimestamp(json_data['sys']['sunset']-28800)
        sunrise = r.strftime("%H:%M:%S")
        sunset = s.strftime("%H:%M:%S")

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Min_Temp: " + str(temp_min) + "°C" + "\n" + "Max_Temp: " + str(temp_max) + "°C" + "\n" + "Pressure: " + str(pressure) + "hPa" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind_speed) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

        label1.config(text=final_info)
        label2.config(text=final_data)

    except:
        pass

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

#define font case
f = ("poppins", 15,"bold")
t = ("poppins", 35,"bold")

#set up textField and bind to getWeather
textField = tk.Entry(canvas,justify="center",width=20,font = t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>',getWeather)

label1 = tk.Label(canvas,font=t)
label1.pack()
label2 = tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()