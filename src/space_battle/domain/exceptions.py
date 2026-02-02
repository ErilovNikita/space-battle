class MovementError(Exception):
    pass

class PositionReadError(MovementError):
    pass

class VelocityReadError(MovementError):
    pass

class PositionWriteError(MovementError):
    pass

class AngleReadError(Exception):
    pass

class AngleWriteError(Exception):
    pass
