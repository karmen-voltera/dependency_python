from ExitMechanism import ExitMechanism

class FutureMechanism (ExitMechanism):

    def __init__(self, 
                 weight_limit: float, 
                 length_limit: float, 
                 size_limit: float, 
                 fragile_capable: bool, 
                 irregular_size_capable: bool,
                 short_side_constraint: float = 0):
        self.weight_limit = weight_limit
        self.length_limit = length_limit
        self.size_limit = size_limit
        self.fragile_capable = fragile_capable
        self.irregular_size_capable = irregular_size_capable
        self.short_side_constraint = short_side_constraint
        

    def within_weight_limit(self, package) -> bool:
        return package.weight <= self.weight_limit
    
    def within_measurement(self, package) -> bool:
        if (self.short_side_constraint > 0):
            return package.longest_side() <= self.length_limit and package.shortest_side() >= self.short_side_constraint
        return package.longest_side() <= self.length_limit
    
    def within_volume_limit(self, package) -> bool:
        return package.volume() <= self.size_limit
    
    def can_handle_fragile(self) -> bool:
        return self.fragile_capable
    
    def can_handle_irregular_size(self):
        return self.irregular_size_capable