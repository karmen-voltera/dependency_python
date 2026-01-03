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

from Error import DimensionError, WeightError, FragileItemError, DestinationError, DispatchError
from Package import Package
from ExitMechanism import ExitMechanism

class DispatchDesk():
    # this is where the business logic is
    # maybe specify a max weight and size for all of the packages it can handle?
    # this receives the package and exit mechanism
    # validates that all required information is there for the package

    def can_dispatch(self, package: Package, exit_mechanism: ExitMechanism) -> bool:
        valid_countries = ['Canada', 'USA']
        if not any(country in package.destination for country in valid_countries):
            raise DestinationError("We do not service your area")
        if not exit_mechanism.within_weight_limit(package) and package.weight < 0:
            #put weight < 0 check here as it applies to all of the mechanisms
            raise WeightError()
        if not exit_mechanism.within_volume_limit(package):
            raise DimensionError("Package volume exceeds limit")
        if not exit_mechanism.within_measurement(package):
            raise DimensionError("Package does not meet length limits for this exit mechanism")
        if package.fragile and not exit_mechanism.can_handle_fragile():
            raise FragileItemError()
        
        return True
    
    def dispatch_package(self, package: Package, exit_mechanism: ExitMechanism) -> str:
        result= exit_mechanism.move_package(package)
        if not result:
            raise DispatchError("Failed to dispatch package using exit mechanism")
        return "Successfully dispatched package"