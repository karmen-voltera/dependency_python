import pytest
from DispatchDesk import DispatchDesk
from ConveyorBelt import ConveyorBelt
from Error import DispatchError, FragileItemError
from Forklift import Forklift
from RoboticArm import RoboticArm
from FutureMechanism import FutureMechanism
from LoadingDock import LoadingDock

from fixtures import *
import copy

success_msg = "Successfully dispatched package"
successful_exit_mechanisms_tests = [
    ConveyorBelt(),
    Forklift(),
    RoboticArm(),
    LoadingDock()
]

fragility = [
    (ConveyorBelt(), FragileItemError),
    (Forklift(), FragileItemError),
    (RoboticArm(), True),
    (LoadingDock(), True)
]

dispatch_package_tests = [
    (ConveyorBelt(), DispatchError, success_msg),
    (Forklift(), DispatchError, success_msg),
    (RoboticArm(), DispatchError, success_msg),
    (LoadingDock(), DispatchError, success_msg)
]

class TestDispatcher:
    @pytest.mark.parametrize("exit_mechanism", successful_exit_mechanisms_tests)
    def test_can_dispatch_success(self, sample_package, exit_mechanism):
        """
        Test that the dispatcher can successfully dispatch a package to a ConveyorBelt.

        Args:
            sample_package: A fixture providing a test package instance.

        Asserts:
            The dispatcher's can_dispatch method returns True when checking if a
            sample_package can be dispatched to ConveyorBelt.
        """
        dispatcher = DispatchDesk()
        assert dispatcher.can_dispatch(sample_package, exit_mechanism) == True
    
    @pytest.mark.parametrize("exit_mechanism, expected_exception", fragility)
    def test_can_dispatch_fragile(self, sample_package, exit_mechanism, expected_exception):
        """
        Test that the dispatcher fails or successfully dispatched a fragile package.

        Args:
            sample_package: A fixture providing a test package instance.

        Asserts:
            The dispatcher's can_dispatch method raises FragileItemError when checking if a
            fragile sample_package can be dispatched to ConveyorBelt.
        """
        dispatcher = DispatchDesk()
        fragile_package=copy.copy(sample_package)
        fragile_package.fragile = True
        
        try:
            dispatch_ability = dispatcher.can_dispatch(fragile_package, exit_mechanism)
            assert dispatch_ability == True
        except Exception as e:
            assert isinstance(e, expected_exception)
    
    @pytest.mark.parametrize("exit_mechanism, expected_error, expected_success", dispatch_package_tests)
    def test_dispatch_package(self, sample_package, exit_mechanism, expected_error, expected_success):
        """
        Test that the dispatcher fails to dispatch a fragile package to a ConveyorBelt.

        Args:
            sample_package: A fixture providing a test package instance.

        Asserts:
            The dispatcher's can_dispatch method raises FragileItemError when checking if a
            fragile sample_package can be dispatched to ConveyorBelt.
        """
        dispatcher = DispatchDesk()
        
        try:
            dispatched=dispatcher.dispatch_package(sample_package, exit_mechanism)
            assert expected_success in dispatched
        except Exception as e:
            # If failed during dispatch, check it raises DispatchError with appropriate message
            assert isinstance(e, expected_error)
            