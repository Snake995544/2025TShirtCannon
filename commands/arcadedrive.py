import typing

import commands2
from subsystems.drivetrain import arcadeDrive

class ArcadeDrive(commands2.Command):
    def __init__(self, arcade_drive: arcadeDrive, y: typing.Callable[[], float], z: typing.Callable[[], float]) -> None:
        super().__init__()
        self.arcade_drive = arcade_drive
        self.y = y
        self.z = z
        self.addRequirements(arcade_drive)

    def execute(self) -> None:
        self.arcade_drive.arcadeDrive(self.y(), self.z())

    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted=False) -> None:
        self.arcade_drive.arcadeDrive(0, 0)