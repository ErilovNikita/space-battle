from abc import ABC, abstractmethod
from typing import Protocol

from .value_objects import Vector


class Movable(Protocol):
    def get_position(self) -> Vector: ...
    def get_velocity(self) -> Vector: ...
    def set_position(self, position: Vector) -> None: ...

class Rotatable(ABC):

    @abstractmethod
    def get_angle(self) -> float: ...

    @abstractmethod
    def set_angle(self, angle: float) -> None: ...
