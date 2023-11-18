# calculate and return the height of a column of water from a tower height and a tank wall height
def water_column_height(tower_height, tank_height):
    h = tower_height + ((3*tank_height)/4)
    return h

# calculate and return the pressure caused by Earth’s gravity pulling on the water stored in an elevated tank.
def pressure_gain_from_water_height(height):
    p =  998.2
    g = 9.80665
    Pa = (p*g*height)/1000
    return Pa

# calculate and return the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    loss = (- friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000*pipe_diameter)
    return loss