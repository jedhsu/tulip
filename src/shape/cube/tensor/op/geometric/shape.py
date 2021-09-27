class ShapingOperator(ArrayOperator):
    Reshape = jnp.reshape

    AtLeast1D = jnp.atleast_1d
    AtLeast2D = jnp.atleast_2d
    AtLeast3D = jnp.atleast_3d

    Roll = jnp.roll

    Squeeze = jnp.squeeze

    Transpose = jnp.transpose


class ShapeProperty:
    Shape = jnp.shape
    NumDimensions = jnp.ndim
