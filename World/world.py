import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="tahiry",
    database='world_x',
    password="3v2nKH8x2cgJjMJC",
    port=3306
)

cursor = db.cursor()

city = input('City to Find: ')

query = f"SELECT country.population, country.name FROM world.city INNER JOIN country ON city.CountryCode = country.Code WHERE city.name = '{city}'"
cursor.execute(query)
city_details = cursor.fetchall()

print(city_details)