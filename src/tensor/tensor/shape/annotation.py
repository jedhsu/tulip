"""

    *Shape,   [Annotation]*

"""
from ._shape import Shape

__all__ = ["Annotation"]


class Annotation(
    Shape,
):
    @classmethod
    def __class_getitem__(
        cls,
        item: tuple[int],
    ) -> tuple[int]:
        if isinstance(
            item,
            tuple,
        ):
            return item
        else:
            return (item,)
