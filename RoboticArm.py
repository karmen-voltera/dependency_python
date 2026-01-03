from ExitMechanism import ExitMechanism
from random import randint

class RoboticArm (ExitMechanism):
    # specify weight and size limits here for this specific exit mechanism
    def within_weight_limit(self, package) -> bool:
        return package.weight <= 50
    
    def within_measurement(self, package) -> bool:
        return package.longest_side() <= 75
    
    def within_volume_limit(self, package) -> bool:
        max_size = 75 * 50 * 20
        return package.volume() <= max_size
    
    def can_handle_fragile(self) -> bool:
        return True
    
    def can_handle_irregular_size(self):
        return True
    