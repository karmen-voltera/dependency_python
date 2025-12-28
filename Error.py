class DimensionError(Exception):
    def __init__(self, message="Invalid dimensions."):
        super().__init__(message)
class WeightError(Exception):
    def __init__(self, message="Invalid weight."):
        super().__init__(message)
class DestinationError(Exception):
    def __init__(self, message="Invalid destination."):
        super().__init__(message)
class FragileItemError(Exception):
    def __init__(self, message="Fragile item cannot be handled by this exit mechanism."):
        super().__init__(message)