from space_battle.domain.value_objects import Vector


class SpaceObject:
    def __init__(self, position: Vector, velocity: Vector):
        self._position = position
        self._velocity = velocity

    def get_position(self) -> Vector:
        return self._position

    def get_velocity(self) -> Vector:
        return self._velocity

    def set_position(self, position: Vector) -> None:
        self._position = position
