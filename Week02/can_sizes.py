'''Compute and print the storage efficiency for each of the following 12 steel can sizes.'''
import math

# Dictionary of cans [radius, height, cost per can in $]
cans = {
    "#1 Picnic": [6.83, 10.16, 0.28],
    "#1 Tall": [7.78, 11.91, 0.43],
    "#2": [8.73, 11.59, 0.45],
    "#2.5": [10.32, 11.91, 0.61],
    "#3 Cylinder": [10.79, 17.78, 0.86],
    "#5": [13.02, 14.29, 0.83],
    "#6Z": [5.40, 8.89, 0.22],
    "#8Z short": [6.83, 7.62, 0.26],
    "#10": [15.72, 17.78, 1.53],
    "#211": [6.83, 12.38, 0.34],
    "#300": [7.62, 11.27, 0.38],
    "#303": [8.10, 11.11, 0.42]
}

def main():
    best_cost_efficiency = ""
    best_storage_effieciency = ""

    # Loop through Can dictionary
    for can, specs in cans.items():
        storage_efficiency = compute_storage_efficiency(can, specs[0], specs[1])
        volume = compute_volume(specs[0], specs[1])
        cost_efficiency = compute_cost_efficiency(volume, specs[2])

        print(f"{can} {storage_efficiency:.2f} {cost_efficiency:.0f}")


def compute_storage_efficiency(can, radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency


def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    result = 2*math.pi * radius * (radius + height)
    return result

def compute_cost_efficiency(volume, cost):
    result = volume / cost
    return result

main()