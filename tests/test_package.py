from Package import Package
import pytest
import Error
from fixtures import *

def invalid_destination_parameters():
    dimensions = {'width': 10.0, 'length': 15.0, 'height': 5.0}
    fragile = False
    irregular_size = False
    weight = 20.0
    invalid_destination_parameters = [
        "", 
        None #invalid
        ]
    
    invalid_destinations = []
    for i, destination in enumerate(invalid_destination_parameters):
        invalid_destinations.append((dimensions, weight, fragile, irregular_size, destination, Error.DestinationError))
    
    return invalid_destinations

def missing_dimension_keys():
    invalid_dimensions_parameters=[
        {'width': 10.0, 'length': 15.0},  # Missing 'height'
        {'length': 15.0, 'height': 5.0},  # Missing 'width'
        {'width': 10.0, 'height': 5.0},   # Missing 'length'
    ]
    weight = 20.0
    fragile = False
    irregular_size = False
    destination = "123 Main St, Anytown, USA"

    missing_keys = []
    for i, dim in enumerate(invalid_dimensions_parameters):
        missing_keys.append((dim, weight, fragile, irregular_size, destination, Error.DimensionError))
    
    return missing_keys

def invalid_weight_values():
    dimensions = {'width': 10.0, 'length': 15.0, 'height': 5.0}
    fragile = False
    irregular_size = False
    destination = "123 Main St, Anytown, USA"
    invalid_weight_parameters=[
        0.0, # invalid
        -5.0 #invalid
    ]

    invalid_weights = []
    for i, weight in enumerate(invalid_weight_parameters):
        invalid_weights.append((dimensions, weight, fragile, irregular_size, destination, Error.WeightError))
    
    return invalid_weights

class TestPackage:

    def test_successful_creation(self, sample_package, sample_parameters):
        assert sample_package.dimensions == sample_parameters[0]
        assert sample_package.weight == sample_parameters[1]
        assert sample_package.fragile == sample_parameters[2]
        assert sample_package.irregular_size == sample_parameters[3]
        assert sample_package.destination == sample_parameters[4]

    @pytest.mark.parametrize("dim, weight, fragile, irregular_size, destination, expected_exception", missing_dimension_keys())
    def test_missing_dimension_key(self, dim, weight, fragile, irregular_size, destination, expected_exception):
        with pytest.raises(expected_exception) as e:
            Package(dim, weight, fragile, irregular_size,destination)
        assert "Invalid dimensions" in str(e.value)

    @pytest.mark.parametrize("dim, weight, fragile, irregular_size, destination, expected_exception", invalid_weight_values())
    def test_invalid_weight(self, dim, weight, fragile, irregular_size, destination, expected_exception):
        with pytest.raises(expected_exception) as e:
            Package(dim, weight, fragile, irregular_size, destination)
        assert "Invalid weight" in str(e.value)


    def test_volume_calculation(self, sample_package, sample_parameters):
        expected_volume = sample_parameters[0]['width'] * sample_parameters[0]['length'] * sample_parameters[0]['height']
        assert sample_package.volume() == expected_volume


    def test_longest_side(self, sample_package, sample_parameters):
        expected_longest_side = sample_parameters[0]['length']
        assert sample_package.longest_side() == expected_longest_side

    def test_shortest_side(self, sample_package, sample_parameters):
        expected_shortest_side = sample_parameters[0]['height']
        assert sample_package.shortest_side() == expected_shortest_side