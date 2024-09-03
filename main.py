import tkinter as tk
import requests

def get_weather(lat):
    api_key = "14558c394172bb890d680f1901b67583"  # You need to replace this with your API key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={14.99}&lon={8.66}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        city_name.config(text=data["name"])
        weather.config(text=data["weather"][0]["description"].capitalize())
        temp.config(text=f"{data['main']['temp']}°C")
    else:
        city_name.config(text="City not found")
        weather.config(text="")
        temp.config(text="")

def on_submit():
    city = city_entry.get()
    get_weather(city)

# Create the main window
root = tk.Tk()
root.title("Weather Prediction")

# Widgets
city_label1 = tk.Label(root, text="Enter lat:")
city_label1.grid(row=0, column=0, padx=10, pady=5)



city_entry = tk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=0, column=2, padx=10, pady=5 )

city_name = tk.Label(root, font=("Arial", 20))
city_name.grid(row=1, column=0, columnspan=3, pady=5)

weather = tk.Label(root, font=("Arial", 16))
weather.grid(row=2, column=0, columnspan=3, pady=5)

temp = tk.Label(root, font=("Arial", 16))
temp.grid(row=3, column=0, columnspan=3, pady=5)

root.mainloop()
