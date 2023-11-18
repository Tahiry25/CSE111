from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest

towers = [
    # [Tower Height, Tank Wall Height, Expected Water Column Height]
    [0.0, 0.0, 0.0],
    [0.0, 10.0, 7.5],
    [25.0, 0.0, 25.0],
    [48.3, 12.8, 57.9]
]

tanks = [
    # [Height, Expected Pressure, Approx Absolute Tolerance]
    [0.0, 0.000, 0.001],
    [30.2, 295.628, 0.001],
    [50.0, 489.450, 0.001]
]

pipes = [
    # Pipe Diameter, Pipe Length, Friction Factor, Fluid Velocity, Expected Pressure Loss, approx Absolute Tolerance
    [0.048692, 0.00, 0.018, 1.75, 0.000, 0.001],
    [0.048692, 200.00, 0.000, 1.75, 0.000, 0.001],
    [0.048692, 200.00, 0.018, 0.00, 0.000, 0.001],
    [0.048692, 200.00, 0.018, 1.75, -113.008, 0.001],
    [0.048692, 200.00, 0.018, 1.65, -100.462, 0.001],
    [0.286870, 1000.00, 0.013, 1.65, -61.576, 0.001],
    [0.286870, 1800.75, 0.013, 1.65, -110.884, 0.001],
]

def test_water_column_height():
    for t in towers:
        assert water_column_height(t[0], t[1]) == t[2]

def test_pressure_gain_from_water_height():
    for tank in tanks:
        assert approx(pressure_gain_from_water_height(tank[0]), abs=tank[2]) == tank[1]

def test_pressure_loss_from_pipe():
    for pipe in pipes:
        pressure_loss = pressure_loss_from_pipe(pipe[0], pipe[1], pipe[2], pipe[3])
        assert approx(pressure_loss, abs=pipe[5]) == pipe[4]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])