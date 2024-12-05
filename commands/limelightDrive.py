import commands2
from subsystems.drivetrain import arcadeDrive
from subsystems.limelight import limelightSystem
class limelightDriveCommand(commands2.Command):
    def __init__(self, arcadedrive: arcadeDrive, limelight: limelightSystem) -> None:
        super().__init__()
        self.drivetrain = arcadedrive
        self.limelight = limelight
        self.addRequirements(arcadedrive)
        self.addRequirements(limelight)
    def execute(self) -> None:
        if self.limelight.get_results() == False:
            self.drivetrain.arcadeDrive(10, 0)
        elif self.limelight.get_results() % 2 == 0:
            # Turn right
            self.drivetrain.arcadeDrive(0, -10)
        elif self.limelight.get_results() % 2 == 1:
            # Turn left
            self.drivetrain.arcadeDrive(0, 10)
    def isFinished(self) -> bool:
        return False
    def end(self, interrupted=False) -> None:
        pass
