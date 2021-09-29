

pub trait ScalarMul: X where X: TensorOp + BinOp<Tensor, Tensor> + Props, Props: Assoc, OpCommut, Dist {
    fn smul_assoc();

    fn glimpse2 {
        ∀x, y, w. smul(smul(x, y), w) = smul(x, smul(y, w))
    }

    fn glimpse3 {
// ∀x, y, w. smul(ewadd(x, y), w) = ewadd(smul(x, w), smul(y, w))

// ∀x, y, w. smul(ewmul(x, y), w) = ewmul(x, smul(y, w))
// }


∀x, w. smul(transpose(x), w) = transpose(smul(x, w))
∀x, y, w. smul(matmul(x, y), w) = matmul(x, smul(y, w))
