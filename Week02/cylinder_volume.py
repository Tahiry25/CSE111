import math

height = float(input("Enter the height of a cylinder: "))
radius = float(input("Enter the radius of a cylinder: "))

def print_cylinder_volume(height, radius):
    volume = math.pi * radius**2 * height
    return volume

print(f"Cylinder volume: {print_cylinder_volume(height, radius):.2f}")