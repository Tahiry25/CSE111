'''Compute and print the storage efficiency for each of the following 12 steel can sizes.'''
import math

# Dictionary of cans [radius, height, cost per can in $]
cans = {
    "#1 Picnic": [6.83, 10.16, 0.28],
    "#1 Tall": [7.78, 11.91, 0.43],
    "#2": [8.73, 11.59, 0.45],
    "#2.5": [10.32, 11.91, 0.61]
}

def main():
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