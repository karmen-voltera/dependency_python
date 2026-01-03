from abc import ABC, abstractmethod
from random import randint

from Error import DispatchError

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
    def within_volume_limit(self, package) -> bool:
        """Is the volume of the package within the mechanism's limits?"""
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
    def within_measurement(self, package) -> bool:
        """Is the longest side of the package within the mechanism's limits?"""
        pass

    #because all concrete classes use the same, I just implemented it here, otherwise, each concrete class would have its own implementation
    def move_package(self, package) -> bool:
        """Move package using exit mechanism"""
        if (randint(1, 100) <= 50):
            return True
        return False
