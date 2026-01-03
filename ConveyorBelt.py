from ExitMechanism import ExitMechanism

class ConveyorBelt (ExitMechanism):
    # specify weight and size limits here for this specific exit mechanism
    def within_weight_limit(self, package) -> bool:
        return package.weight <= 100
    
    def within_measurement(self, package) -> bool:
        return package.longest_side() <= 200
    
    def within_volume_limit(self, package) -> bool:
        max_size = 100 * 150 * 200 
        return package.volume() <= max_size
    
    def can_handle_fragile(self) -> bool:
        return False
    
    def can_handle_irregular_size(self):
        return True
    