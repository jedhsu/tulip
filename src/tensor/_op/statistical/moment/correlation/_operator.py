"""

    *Correlation Inference*

"""
from .._operator import MomentInference

__all__ = ["CorrelationInference"]


class CorrelationInference(
    MomentInference,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(CorrelationInference, self).__init__(
            *args,
            **kwargs,
        )
