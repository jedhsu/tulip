"""

    *Shape,   [Display]*

"""
from ._shape import Shape

__all__ = ["Display"]


class Display(
    Shape,
):
    def __repr__(self) -> str:
        return "[" + " - ".join([str(part) for part in self]) + "]"


class Test:
    @staticmethod
    def vector():
        return "[5]"

    @staticmethod
    def grid():
        return "[5 - 5]"

    @staticmethod
    def threetope():
        return "[5 - 5 - 5]"
