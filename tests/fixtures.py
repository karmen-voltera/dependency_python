import pytest
from Package import Package

@pytest.fixture
def sample_parameters():
    dimensions = {'width': 35.0, 'length': 40.0, 'height': 30.0}
    weight = 20.0
    fragile = False
    irregular_size = False
    destination = "123 Main St, Anytown, USA"
    return (dimensions, weight, fragile, irregular_size, destination)

@pytest.fixture
def sample_package(sample_parameters):
    return Package(*sample_parameters)