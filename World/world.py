import mysql.connector
import tkinter as tk

window = tk.Tk()
window.geometry("300x400")
window.title("City Finder")
label = tk.Label(window, text="Enter name of a city", font=('Arial', 20))
label.pack(padx=50, pady=(10,5))
textbox = tk.Entry(window, font=('Arial', 16))
textbox.pack(pady=10, padx=20)
button = tk.Button(window, text="Get City Details")
button.pack()

button.bind("<Button-1>", print('test'))

window.mainloop()


db = mysql.connector.connect(
    host="192.168.0.163",
    user="root",
    database='world',
    password="hAoZSuW6pc8tty3Q",
    port=3606
)
cursor = db.cursor()

def main():
    city_name = input('City to Find: ')
    try:
        city_details = get_city_details(city_name)
        print(city_details)
    except:
        print('Sorry, city not found.')

    try:
        capital = get_capital(city_details[3])
        print(capital)
    except:
        print('Country not found.')


# Retrieve city details from database (country code, country name, population, capitalId)
def get_city_details(event):
    city = textbox.get()
    query = f"SELECT country.code, country.name, country.population, country.capital FROM world.city INNER JOIN country ON city.CountryCode = country.Code WHERE city.name = '{city}'"
    cursor.execute(query)
    city_details = cursor.fetchall()
    return city_details[0]

# Find Capital of a country
def get_capital(code):
    query = f"SELECT city.name FROM world.city INNER JOIN country ON city.CountryCode = country.code where city.id = '{code}'"
    cursor.execute(query)
    capital = cursor.fetchall()
    return capital[0][0]


# Call main to start this program.
if __name__ == "__main__":
    main()