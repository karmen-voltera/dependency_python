class Package:

    def __init__(self, dimensions: dict[str, float], weight: float, fragile: bool, destination: str):
        
        self.dimensions = dimensions
        if dimensions.keys() != {'width', 'length', 'height'}:
            raise ValueError("Dimensions must contain exactly 'width', 'length', and 'height' keys")
        self.weight = weight
        self.fragile = fragile
        self.destination = destination

    def volume(self) -> float:
        return self.dimensions['width'] * self.dimensions['length'] * self.dimensions['height']
    
    def longest_side(self) -> float:
        return max(self.dimensions['width'], self.dimensions['length'], self.dimensions['height'])