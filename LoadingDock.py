from ExitMechanism import ExitMechanism

class LoadingDock (ExitMechanism):
    # defines the physical constraints for this exit mechanism

    def within_weight_limit(self, package) -> bool:
        return package.weight <= 1000
    
    def within_measurement(self, package) -> bool:
        # shortest_side = min(package.dimensions['width'], package.dimensions['length'], package.dimensions['height'])
        #forklift would have a minimum length as it cannot lift things between the forks
        return package.longest_side() <= 1000
    
    def within_volume_limit(self, package) -> bool:
        max_size = 500 * 1000 * 1000 
        return package.volume() <= max_size
    
    def can_handle_fragile(self) -> bool:
        return True
    
    def can_handle_irregular_size(self):
        return True