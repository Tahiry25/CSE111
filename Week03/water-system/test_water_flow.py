from water_flow import water_column_height,\
            pressure_gain_from_water_height,\
            pressure_loss_from_pipe, pressure_loss_from_fittings,\
            reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi

from pytest import approx
import pytest

towers = [
    # [Tower Height, Tank Wall Height, Expected Water Column Height]
    [0.0, 0.0, 0.0],
    [0.0, 10.0, 7.5],
    [25.0, 0.0, 25.0],
    [48.3, 12.8, 57.9]
]
def test_water_column_height():
    for t in towers:
        assert water_column_height(t[0], t[1]) == t[2]

tanks = [
    # [Height, Expected Pressure, Approx Absolute Tolerance]
    [0.0, 0.000, 0.001],
    [30.2, 295.628, 0.001],
    [50.0, 489.450, 0.001]
]
def test_pressure_gain_from_water_height():
    for tank in tanks:
        assert approx(pressure_gain_from_water_height(tank[0]), abs=tank[2]) == tank[1]

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
def test_pressure_loss_from_pipe():
    for pipe in pipes:
        pressure_loss = pressure_loss_from_pipe(pipe[0], pipe[1], pipe[2], pipe[3])
        assert approx(pressure_loss, abs=pipe[5]) == pipe[4]

fittings = [
    [0.00, 3, 0.000, 0.001],
    [1.65, 0, 0.000, 0.001],
    [1.65, 2, -0.109, 0.001],
    [1.75, 2, -0.122, 0.001],
    [1.75, 5, -0.306, 0.001],
]
def test_pressure_loss_from_fittings():
    for fitting in fittings:
        pressure_loss = pressure_loss_from_fittings(fitting[0], fitting[1])
        assert approx(pressure_loss, abs=fitting[3]) == fitting[2]

pipes_water = [
    [0.048692, 0.00, 0, 1],
    [0.048692, 1.65, 80069, 1],
    [0.048692, 1.75, 84922, 1],
    [0.286870, 1.65, 471729, 1],
    [0.286870, 1.75, 500318, 1],
]
def test_reynolds_number():
    for pw in pipes_water:
        Rn = reynolds_number(pw[0], pw[1])
        assert approx(Rn, pw[3]) == pw[2]


pressure_loss_from_pipe_reduction_data = [
    [0.28687, 0.00, 1, 0.048692, 0.000, 0.001],
    [0.28687, 1.65, 471729, 0.048692, -163.744, 0.001],
    [0.28687, 1.75, 500318, 0.048692, -184.182, 0.001],
]

def test_pressure_loss_from_pipe_reduction():
    for data in pressure_loss_from_pipe_reduction_data:
        p = pressure_loss_from_pipe_reduction(data[0], data[1], data[2], data[3])
        assert approx(p, abs=data[5]) == data[4]

kPa = [
    [158.7, 23.0, 0.1],
    [200.0, 29.0, 0.1]
]
def test_kpa_to_psi():
    for u in kPa:
        psi = kPa_to_psi(u[0])
        assert approx(psi, abs=u[2]) == u[1]


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])