import mysql.connector
import tkinter as tk

db = mysql.connector.connect(
    host="192.168.0.163",
    user="root",
    database='world',
    password="hAoZSuW6pc8tty3Q",
    port=3606
)
cursor = db.cursor()

def main():
    root = tk.Tk()
    root.geometry("300x400")
    root.title("City Finder")
    populate_main_window(root)
    root.mainloop()

def populate_main_window(root):
    lbl_city = tk.Label(root, text="Enter name of a city", font=('Arial', 20))
    lbl_city.pack(pady=10, padx=20)
    textbox = tk.Entry(root, font=('Arial', 16))
    textbox.pack()
    submit = tk.Button(root, text="Get City Details")
    submit.pack()

    def get_city_details(event):
        city = textbox.get()
        query = f"SELECT country.code, country.name, city.population, country.capital, city.name FROM world.city INNER JOIN country ON city.CountryCode = country.Code WHERE city.name LIKE '%{city}%'"
        cursor.execute(query)
        city_details = cursor.fetchall()[0]
        lbl_country = tk.Label(root, text="Country: ")
        lbl_country.pack(side=tk.LEFT, pady=10)
        country = tk.Label(root, text=f"{city_details[1]}")
        country.pack(side=tk.RIGHT, pady=10)

    submit.bind("<Button-1>", get_city_details)
# Call main to start this program.
if __name__ == "__main__":
    main()