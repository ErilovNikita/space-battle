import pytest
from space_battle.domain.exceptions import AngleReadError, AngleWriteError
from space_battle.domain.protocols import Rotatable
from space_battle.use_cases.rotate_object import RotateObjectUseCase

from tests.logging_helper import expect, result, scenario


@pytest.fixture
def rotatable_obj() -> Rotatable:
    class Obj(Rotatable):
        def __init__(self, angle: float = 0.0) -> None:
            self._angle = angle

        def get_angle(self) -> float:
            return self._angle

        def set_angle(self, angle: float) -> None:
            self._angle = angle

    return Obj()


def test_rotate_object_success(rotatable_obj:Rotatable) -> None:
    scenario("Rotate object by 90 degrees")
    expect("New angle should be current + 90 degrees")

    rotatable_obj.set_angle(45.0)
    RotateObjectUseCase().execute(rotatable_obj, 90.0)

    assert rotatable_obj.get_angle() == 135.0
    result("Object rotated to 135° as expected")


def test_rotate_object_wrap_around(rotatable_obj:Rotatable) -> None:
    scenario("Rotate object past 360 degrees")
    expect("Angle should wrap around 360")

    rotatable_obj.set_angle(350.0)
    RotateObjectUseCase().execute(rotatable_obj, 20.0)

    assert rotatable_obj.get_angle() == 10.0
    result("Object angle wrapped to 10° as expected")


def test_rotate_object_read_error() -> None:
    scenario("Rotate object when get_angle fails")
    expect("Should raise AngleReadError")

    class Obj(Rotatable):
        def get_angle(self) -> float:
            raise RuntimeError

        def set_angle(self, angle: float) -> None:
            pass

    with pytest.raises(AngleReadError):
        RotateObjectUseCase().execute(Obj(), 30.0)

    result("AngleReadError raised as expected")


def test_rotate_object_write_error() -> None:
    scenario("Rotate object when set_angle fails")
    expect("Should raise AngleWriteError")

    class Obj(Rotatable):
        def __init__(self) -> None:
            self._angle = 0.0

        def get_angle(self) -> float:
            return self._angle

        def set_angle(self, angle: float) -> None:
            raise RuntimeError

    with pytest.raises(AngleWriteError):
        RotateObjectUseCase().execute(Obj(), 30.0)

    result("AngleWriteError raised as expected")
