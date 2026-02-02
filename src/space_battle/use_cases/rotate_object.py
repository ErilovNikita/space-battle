from math import fmod

from space_battle.domain.exceptions import AngleReadError, AngleWriteError
from space_battle.domain.protocols import Rotatable


class RotateObjectUseCase:

    def execute(self, obj: Rotatable, delta_angle: float) -> None:
        angle = self._read_angle(obj)
        new_angle = fmod(angle + delta_angle, 360.0)
        self._write_angle(obj, new_angle)

    @staticmethod
    def _read_angle(obj: Rotatable) -> float:
        try:
            return obj.get_angle()
        except Exception as exc:
            raise AngleReadError('Cannot read angle') from exc

    @staticmethod
    def _write_angle(obj: Rotatable, angle: float) -> None:
        try:
            obj.set_angle(angle)
        except Exception as exc:
            raise AngleWriteError('Cannot write angle') from exc
