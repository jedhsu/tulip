from ._shape import Shape as _Shape
from .annotation import Annotation
from .display import Display

__all__ = ["Shape"]


class Shape(
    Annotation,
    Display,
    _Shape,
):
    pass
