import tkinter as tk
from PIL import ImageTk, Image
import requests
from tkinter import font

#API CALL = api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

height= 500
width=600


def get_weather(city):
    weather_key = '9725852c66767bb568e1e38e4cc9d0df'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        result = f'City: {name}\n Weather Description: {desc}\n Temperature: {temp}'
    except:
        result = "Are you sure this is a real city?"

    return result





#Tkinter
root = tk.Tk()
root.resizable(0, 0)
root.title('WeatherApp')

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

#Background Image set with PIL
background_image = ImageTk.PhotoImage(Image.open("bgimg.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


title = tk.Label(root, text="Weather App", font=('Ebrima', 15), bg='#7aeb98')
title.place(relx=0.5, rely=0.05, relwidth=0.3, relheight=0.07, anchor='n')

frame = tk.Frame(root, bg='#7aeb98', bd=4)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.06, anchor='n')

entry = tk.Entry(frame, font='Ebrima')
entry.place(relwidth= 0.65, relheight=1)


#Button
btn = tk.Button(frame, text="Check Weather", font='Ebrima', command=lambda:get_weather(entry.get()), cursor='arrow')
btn.place(relx= 0.7, rely=0, relwidth= 0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#7aeb98', bd=4)
lower_frame.place(relx = 0.5, rely= 0.25, relwidth= 0.75, relheight= 0.6, anchor='n')


label = tk.Label(lower_frame, text="Weather information will be shown here.", font=('Ebrima', 15))
label.place(relx= 0.05, rely=0.05, relwidth= 0.9, relheight=0.5)


root.mainloop()