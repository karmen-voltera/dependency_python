from abc import ABC, abstractmethod

# Exit mechanism interface
# this has to describe what needs to happen, not HOW
# success or failure

# interface ExitMechanism:
    # method to determine if weight is within limits
    # method to determine if size is within limits
    # can it handle fragile items?
    # need to return success or failure

class ExitMechanism(ABC):
    @abstractmethod
    def within_weight_limit(self, package) -> bool:
        """Can the mechanism handle the weight of the package?"""
        pass

    @abstractmethod
    def within_size_limit(self, package) -> bool:
        """Is the size of the package within the mechanism's limits?"""
        pass

    @abstractmethod
    def can_handle_fragile(self, package) -> bool:
        """Can the mechanism handle fragile packages?"""
        pass

    @abstractmethod
    def can_handle_irregular_size(self, package) -> bool:
        """Can the mechanism handle irregularly shaped packages?"""
        pass

    @abstractmethod
    def within_length(self, package) -> bool:
        """Is the longest side of the package within the mechanism's limits?"""
        pass

    @abstractmethod
    def move_package(self, package) -> bool:
        """Move package using exit mechanism"""
        pass
