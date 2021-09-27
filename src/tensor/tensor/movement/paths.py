"""

    *Movement Space*

  A set of movement paths.

"""
from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

from ._movement import Movement
from .path import MovementPath

__all__ = ["MovementPaths"]


@dataclass
class MovementPaths(
    list[tuple[int, ...]],
    Movement,
):
    def __init__(
        self,
        *path: tuple[int, ...],
    ):
        # check all equal lengths
        lengths = [len(path) for path in [*path]]
        assert all(el == lengths[0] for el in lengths)
        super(MovementPaths, self).__init__(
            [*path],
        )

    @property
    def dimension(self) -> int:
        return len(self[0])

    def permute_dimensions(
        self,
        dimensions: int,
    ) -> Sequence[tuple[int, ...]]:
        return list(
            combinations(
                range(dimensions),
                self.dimension,
            )
        )

    def into_paths(
        self,
        *,
        dimensions: int,
    ) -> set[MovementPath]:
        # [TODO] SUPER INEFFICIENT
        permutations = self.permute_dimensions(dimensions)
        paths = set()
        for permutation in permutations:
            for movement in self:
                mvmt = [0] * dimensions
                for index, step in zip(permutation, movement):
                    mvmt[index] = step
                paths.add(MovementPath(mvmt))
        return paths


class Test:
    chessboard = MovementPaths(
        (-1,),
        (1,),
    )

    neighborhood = MovementPaths(
        (-1, -1),
        (-1, +1),
        (+1, -1),
        (+1, +1),
    )
