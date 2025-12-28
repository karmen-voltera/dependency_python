from Package import Package
import pytest



def sample_parameters():
    dimensions = {'width': 10.0, 'length': 15.0, 'height': 5.0}
    weight = 20.0
    fragile = False
    destination = "123 Main St, Anytown, USA"
    return dimensions, weight, fragile, destination

@pytest.fixture
def sample_package(sample_parameters):
    dimensions, weight, units, fragile, destination = sample_parameters
    return Package(dimensions, weight, units, fragile, destination)

def dimensions_parameters():
    return [
        {'width': 10.0, 'length': 15.0, 'height': 5.0}, # valid
        {'width': 10.0, 'length': 15.0},  # Missing 'height'
        {'length': 15.0, 'height': 5.0},  # Missing 'width'
        {'width': 10.0, 'height': 5.0},   # Missing 'length'
    ]

def weight_parameters():
    return [
        10.0, # valid
        0.0, # invalid
        -5.0 #invalid
    ]

def destination_parameters():
    return [
        "123 Main St, Anytown, USA", #valid
        "" #invalid
        ]

def unsuccessful_packages():
    invalid_package_def = []
    missing_dimensions = []
    return []


class TestPackage:

    def test_successful_creation(self):
        dimensions = {'width': 10.0, 'length': 15.0, 'height': 5.0}
        weight = 20.0
        units = {'weight': 'kg', 'dimensions': 'cm'}
        fragile = False
        destination = "123 Main St, Anytown, USA"
        package = Package(dimensions, weight, units, fragile, destination)
        assert package.dimensions == dimensions
        assert package.weight == weight
        assert package.units == units
        assert package.fragile == fragile
        assert package.destination == destination

    def test_missing_dimension_key(self):
        dimensions = {'width': 10.0, 'length': 15.0}  # Missing 'height'
        weight = 20.0
        units = {'weight': 'kg', 'dimensions': 'cm'}
        fragile = False
        destination = "123 Main St, Anytown, USA"
        with pytest.raises(ValueError) as e:
            Package(dimensions, weight, units, fragile, destination)
        assert "Dimensions must contain exactly 'width', 'length', and 'height' keys" in str(e.value)

    def test_volume_calculation(self, sample_package):
        expected_volume = 10.0 * 15.0 * 5.0
        assert sample_package.volume() == expected_volume


    def test_longest_side(self, sample_package):
        expected_longest_side = 15.0
        assert sample_package.longest_side() == expected_longest_side