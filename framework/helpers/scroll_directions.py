from enum import Enum


class ScrollDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"ScrollDirection.{self.value.upper()}"