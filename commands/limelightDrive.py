import commands2
from commands.arcadedrive import ArcadeDrive
from subsystems.limelight import limelightSystem
class limelightDriveCommand(commands2.CommandBase):
    def __init__(self, arcadedrive: ArcadeDrive, limelight: limelightSystem) -> None:
        super.__init__()
        self.drivetrain = arcadedrive
        self.limelight = limelight
        self.addRequirements(arcadedrive)
        self.addRequirements(limelight)
    def execute(self) -> None:
        if self.limelight.get_results() == False:
            self.drivetrain(lambda: 10, lambda: 0)
        elif self.limelight.get_results() % 2 == 0:
            # Turn right
            self.drivetrain(lambda: 0, lambda: -10)
        elif self.limelight.get_results() % 2 == 1:
            # Turn left
            self.drivetrain(lambda: 0, lambda: 10)
    def isFinished(self) -> bool:
        return False
    def end(self) -> None:
        pass
