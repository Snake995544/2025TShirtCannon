import commands2
import typing
from subsystems.limelight import limelightSystem

class limelightDisplay(commands2.Command):
    def __init__(self, limelight: limelightSystem) -> None:
        super().__init__()
        self.limelight = limelight
        self.addRequirements(limelight)

    def execute(self) -> None:
        # print(self.limelight.get_results().tagId)
        results = self.limelight.get_results()
        print(results.tagId if results else 'none')

    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted=False) -> None:
        pass