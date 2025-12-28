from ExitMechanism import ExitMechanism

class ForkLift (ExitMechanism):
    # defines the physical constraints for this exit mechanism

    def shortest_side(self, package) -> float:
        return min(package.dimensions['width'], package.dimensions['length'], package.dimensions['height'])

    def within_weight_limit(self, package) -> bool:
        return package.weight <= 300
    
    def within_length(self, package) -> bool:
        #forklift would have a minimum length as it cannot lift things between the forks
        return package.longest_side() <= 500 and self.shortest_side(package) >= 30
    
    def within_size_limit(self, package) -> bool:
        max_size = 360 * 450 * 500 
        return package.volume() <= max_size
    
    def can_handle_fragile(self) -> bool:
        return False
    
    def can_handle_irregular_size(self):
        return False
    
    def move_package(self, package) -> bool:
        return True