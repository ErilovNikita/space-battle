import pytest
from space_battle.domain.exceptions import PositionReadError, PositionWriteError, VelocityReadError
from space_battle.domain.value_objects import Vector
from space_battle.use_cases.move_object import MoveObjectUseCase

from tests.logging_helper import expect, result, scenario


class ValidObject:
    position: Vector
    velocity: Vector

    def __init__(self) -> None:
        self.position = Vector(12, 5)
        self.velocity = Vector(-7, 3)

    def get_position(self) -> Vector:
        return self.position

    def get_velocity(self) -> Vector:
        return self.velocity

    def set_position(self, position: Vector) -> None:
        self.position = position


def test_move_object_success() -> None:
    scenario("Move object with valid position and velocity")
    expect("New position should be calculated as position + velocity")

    obj = ValidObject()
    MoveObjectUseCase().execute(obj)

    assert obj.position == Vector(5, 8)

    result("Object moved to (5, 8) as expected")


def test_position_read_error() -> None:
    scenario("Move object when position cannot be read")
    expect("PositionReadError should be raised")

    class Obj:
        def get_position(self) -> Vector:
            raise RuntimeError

        def get_velocity(self) -> Vector:
            return Vector(1, 1)

        def set_position(self, position: Vector) -> None:
            pass

    with pytest.raises(PositionReadError):
        MoveObjectUseCase().execute(Obj())

    result("PositionReadError was raised as expected")


def test_velocity_read_error() -> None:
    scenario("Move object when velocity cannot be read")
    expect("VelocityReadError should be raised")

    class Obj:
        def get_position(self) -> Vector:
            return Vector(1, 1)

        def get_velocity(self) -> Vector:
            raise RuntimeError

        def set_position(self, position: Vector) -> None:
            pass

    with pytest.raises(VelocityReadError):
        MoveObjectUseCase().execute(Obj())

    result("VelocityReadError was raised as expected")


def test_position_write_error() -> None:
    scenario("Move object when position cannot be written")
    expect("PositionWriteError should be raised")

    class Obj:
        def get_position(self) -> Vector:
            return Vector(1, 1)

        def get_velocity(self) -> Vector:
            return Vector(1, 1)

        def set_position(self, position: Vector) -> None:
            raise RuntimeError

    with pytest.raises(PositionWriteError):
        MoveObjectUseCase().execute(Obj())

    result("PositionWriteError was raised as expected")
