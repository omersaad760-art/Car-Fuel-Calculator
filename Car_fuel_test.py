import pytest
from car_fuel import fuelCalculator

@pytest.fixture
def calculator():
    return fuelCalculator()

def test_calculate_fuel(calculator):
    assert calculator.calculate_fuel(200,8) == 16
    

def test_calculate_fuel_invalid(calculator):
    with pytest.raises(ValueError):
        calculator.calculate_fuel(0,6)

def test_calculate_cost(calculator):
    assert calculator.calculate_cost(16,15) == 240
    

def test_calculate_cost_invalid(calculator):
    with pytest.raises(ValueError):
        calculator.calculate_cost(-1,8)

def test_calculate_consumption(calculator):
    assert calculator.calculate_consumption(100,16) == 16
    

def test_calculate_consumption_invalid(calculator):
    with pytest.raises(ValueError):
        calculator.calculate_consumption(0,10)




