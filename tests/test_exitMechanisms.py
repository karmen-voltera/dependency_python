import pytest
from Package import Package
from ConveyorBelt import ConveyorBelt
from Forklift import Forklift
from fixtures import *
import copy

class TestConveyorBelt:
    def test_within_weight_limit(self, sample_package):
        mechanism = ConveyorBelt()
        light_package=copy.copy(sample_package)
        light_package.weight = 50.0
        heavy_package=copy.copy(sample_package)
        heavy_package.weight = 100.0
        
        assert mechanism.within_weight_limit(light_package) == True
        assert mechanism.within_weight_limit(heavy_package) == True
    
    def test_outside_weight_limit(self, sample_package):
        mechanism = ConveyorBelt()
        heavy_package=copy.copy(sample_package)
        heavy_package.weight = 100.1
        assert mechanism.within_weight_limit(heavy_package) == False

    def test_within_volume_limit(self, sample_package):
        mechanism = ConveyorBelt()
        small_package=copy.copy(sample_package)
        small_package.dimensions = {'width': 50.0, 'length': 50.0, 'height': 30.0}
        large_package=copy.copy(sample_package)
        large_package.dimensions = {'width': 100.0, 'length': 150.0, 'height': 200.0}
        assert mechanism.within_volume_limit(small_package) == True
        assert mechanism.within_volume_limit(large_package) == True
    
    def test_outside_volume_limit(self, sample_package):
        mechanism = ConveyorBelt()
        oversized_package=copy.copy(sample_package)
        oversized_package.dimensions = {'width': 101.0, 'length': 150.0, 'height': 200.0}
        assert mechanism.within_volume_limit(oversized_package) == False

    def test_can_handle_fragile(self):
        mechanism = ConveyorBelt()
        assert mechanism.can_handle_fragile() == False

    def test_can_handle_irregular_size(self):
        mechanism = ConveyorBelt()
        assert mechanism.can_handle_irregular_size() == True

class TestForklift:
    def test_within_weight_limit(self, sample_package):
        mechanism = Forklift()
        light_package=copy.copy(sample_package)
        light_package.weight = 500.0
        heavy_package=copy.copy(sample_package)
        heavy_package.weight = 1000.0
        
        assert mechanism.within_weight_limit(light_package) == True
        assert mechanism.within_weight_limit(heavy_package) == True
    
    def test_outside_weight_limit(self, sample_package):
        mechanism = Forklift()
        heavy_package=copy.copy(sample_package)
        heavy_package.weight = 1000.1
        assert mechanism.within_weight_limit(heavy_package) == False

    def test_within_volume_limit(self, sample_package):
        mechanism = Forklift()
        small_package=copy.copy(sample_package)
        small_package.dimensions = {'width': 200.0, 'length': 200.0, 'height': 200.0}
        large_package=copy.copy(sample_package)
        large_package.dimensions = {'width': 500.0, 'length': 1000.0, 'height': 1000.0}
        assert mechanism.within_volume_limit(small_package) == True
        assert mechanism.within_volume_limit(large_package) == False
    
    def test_outside_volume_limit(self, sample_package):
        mechanism = Forklift()
        oversized_package=copy.copy(sample_package)
        oversized_package.dimensions = {'width': 501.0, 'length': 1000.0, 'height': 1000.0}
        assert mechanism.within_volume_limit(oversized_package) == False

    def test_can_handle_fragile(self):
        mechanism = Forklift()
        assert mechanism.can_handle_fragile() == False

    def test_can_handle_irregular_size(self):
        mechanism = Forklift()
        assert mechanism.can_handle_irregular_size() == False

