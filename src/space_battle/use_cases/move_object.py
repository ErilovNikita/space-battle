from space_battle.domain.exceptions import PositionReadError, PositionWriteError, VelocityReadError
from space_battle.domain.protocols import Movable
from space_battle.domain.value_objects import Vector


class MoveObjectUseCase:
    def execute(
        self,
        obj: Movable
    ) -> None:
        try:
            position: Vector = obj.get_position()
        except Exception as exc:
            raise PositionReadError("Cannot read position") from exc

        try:
            velocity: Vector = obj.get_velocity()
        except Exception as exc:
            raise VelocityReadError("Cannot read velocity") from exc

        new_position = position + velocity

        try:
            obj.set_position(new_position)
        except Exception as exc:
            raise PositionWriteError("Cannot write position") from exc

