import requests
import tkinter as tk
from tkinter import messagebox

def get_country_info():
    country = country_entry.get().strip()
    if not country:
        messagebox.showerror("Error", "Please enter a country name!")
        return

    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        if response.status_code == 404:
            messagebox.showerror("Error", "Country not found!")
            return
        data = response.json()[0]

        name = data.get('name', {}).get('common', 'Unknown')
        capital = data.get('capital', ['Unknown'])[0]
        region = data.get('region', 'Unknown')
        population = data.get('population', 'Unknown')
        area = data.get('area', 'Unknown')
        currencies = data.get('currencies', {})
        currency = ', '.join([f"{v.get('name')} ({k})" for k, v in currencies.items()])

        info_label.config(text=f"Country Name: {name}\nCapital: {capital}\nRegion: {region}\nPopulation: {population}\nArea: {area} km²\nCurrency: {currency}")

    except:
        messagebox.showerror("Error", "Failed to retrieve information")

root = tk.Tk()
root.title("Country Information")

country_label = tk.Label(root, text="Enter a country name:")
country_label.pack(pady=5)

country_entry = tk.Entry(root, width=30)
country_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=get_country_info)
search_button.pack(pady=5)

info_label = tk.Label(root, text="", justify="left", anchor="w", width=50, height=10, bg="lightyellow", wraplength=400)
info_label.pack(pady=10)

root.mainloop()
