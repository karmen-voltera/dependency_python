from Error import DestinationError, WeightError, DimensionError
class Package:

    def __init__(self, dimensions: dict[str, float], weight: float, fragile: bool, irregular_size: bool,destination: str):
        
        self.dimensions = dimensions
        if dimensions.keys() != {'width', 'length', 'height'}:
            raise DimensionError()
        self.weight = weight
        if weight <= 0:
            raise WeightError()
        self.fragile = fragile
        self.destination = destination
        self.irregular_size = irregular_size
        if not destination or not isinstance(destination, str):
            raise DestinationError()

    def volume(self) -> float:
        return self.dimensions['width'] * self.dimensions['length'] * self.dimensions['height']
    
    def longest_side(self) -> float:
        return max(self.dimensions['width'], self.dimensions['length'], self.dimensions['height'])
    
    def shortest_side(self) -> float:
        return min(self.dimensions['width'], self.dimensions['length'], self.dimensions['height'])