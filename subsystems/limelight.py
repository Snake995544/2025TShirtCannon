import typing
import commands2
import constants
import wpilib
import limelight
from interfaces.limelight_results import limelightResults

class limelightSystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        limelights = limelight.discover_limelights(debug=True)

        if not limelights:
            raise ValueError("No limelights found")
        
        self.limelight = limelight.Limelight(limelights[0])

    def get_results(self, debug=False) -> typing.Optional[limelightResults]:
        results = self.limelight.get_results()

        if results["botpose_tagcount"] == 0:
            return False

        return limelightResults(results)
