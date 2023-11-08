import math
from datetime import datetime

print(f"Calculate the volume of space inside a car tire.\n")
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

print(f"\nTire size: {w}/{a}R{d}")

v = math.pi * pow(w, 2) * a * (w*a + 2540*d) / 10000000000

print(f"The approximate volume is {v:.2f} liters\n")

today = datetime.now()
formatted_date = today.strftime("%Y-%m-%d")

# ask the user if she wants to buy tires with the dimensions that she entered.
to_purchase = input("Would you like to buy tires with these dimensions? ")

# store phone number in the volumes.txt file along with w, a, d and v.
with open('volumes.txt', 'a') as file:
    if to_purchase == "yes":
        phone_number = input("Please enter you phone number: ")
        file.write(f"{ formatted_date }, {w}, {a}, {d}, {v:.2f} / Phone Number: {phone_number}\n\n")
    else:
        file.write(f"{ formatted_date }, {w}, {a}, {d}, {v:.2f}\n\n")
