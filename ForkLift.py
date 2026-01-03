from ExitMechanism import ExitMechanism

class Forklift (ExitMechanism):

    def within_weight_limit(self, package) -> bool:
        return package.weight <= 1000
    
    def within_measurement(self, package) -> bool:
        #forklift would have a minimum length as it cannot lift things between the forks
        return package.longest_side() <= 500 and package.shortest_side() >= 30
    
    def within_volume_limit(self, package) -> bool:
        max_size = float(360 * 450 * 500) 
        return package.volume() <= max_size
    
    def can_handle_fragile(self) -> bool:
        return False
    
    def can_handle_irregular_size(self):
        return False