'''Compute and print the storage efficiency for each of the following 12 steel can sizes.'''
import math

# Dictionary of can [radius, height, cost per can in $]
cans = {
    "#1 Picnic": [6.83, 10.16, 0.28],
    "#1 Tall": [7.78, 11.91, 0.43],
    "#2": [8.73, 11.59, 0.45],
    "#2.5": [10.32, 11.91, 0.61]
}

def main(can, radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    print(f"{can} {storage_efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    result = 2*math.pi * radius * (radius +height)
    return result

# Loop through Can dictionary
for can, specs in cans.items():
    main(can, specs[0], specs[1])