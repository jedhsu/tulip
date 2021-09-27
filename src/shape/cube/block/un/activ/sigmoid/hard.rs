
pub struct HardSigmoid;

impl Calibrate for Activate<HardSigmoid> {
    inplace: bool

    fn forward(&self, input: Tensor) -> Tensor:
        return F.hardsigmoid(input, self.inplace)
}
