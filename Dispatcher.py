# packages arrive
# what are the sizes and shapes of the packages? Weight of the packages? 
# package leaves by different means

# what does the dispatcher need to do?
# probably need to weigh the package, determine size of the package
# destination
# so we need to know what the constraints are for each type of delivery



# first real exit mechanism
# conveyor belt
# forklift
# need to take into consideration physical constraints like
# weight limits, missing package information, mechanical limitations
# it has to implement the interface
# no business logic unrelated to physically moving the package
# swappable without modifying the dispatch desk

from Error import DimensionError, WeightError, FragileItemError, DestinationError
from Package import Package
from ExitMechanism import ExitMechanism

class DispatchDesk():
    # this is where the business logic is
    # maybe specify a max weight and size for all of the packages it can handle?
    # this receives the package and exit mechanism
    # validates that all required information is there for the package

    def can_dispatch(self, package: Package, exit_mechanism: ExitMechanism) -> bool:
        if not package.destination:
            raise DestinationError
        if not exit_mechanism.within_weight_limit(package):
            raise WeightError
        if not exit_mechanism.within_size_limit(package):
            raise DimensionError
        if not exit_mechanism.within_length(package):
            raise DimensionError
        if package.fragile and not exit_mechanism.can_handle_fragile():
            raise FragileItemError
        
        return True
    
    def dispatch_package(self, package: Package, exit_mechanism: ExitMechanism) -> bool:
        return exit_mechanism.move_package(package)