use crate::ScalarMul;
use crate::TensorOp;
use crate::BinOp;

pub trait ScalarMul: X where X: TensorOp + BinOp<Tensor, Tensor> + Props, Props: Assoc, Dist {
    fn smul_assoc();

    fn glimpse2 {
        ScalarMul(ScalarMul(𝚠, y), w) = ScalarMul(x, ScalarMul(y, w));
    }

    fn glimpse3 {
        ScalarMul(ElAdd(x, y), w) = ElAdd(ScalarMul(x, w), ScalarMul(y, w));
    }

    fn glimpse4 {
        ScalarMul(ElMul(x, y), w) = ElMul(x, ScalarMul(y, w));
    }

    fn glimpse5 {ScalarMul(Transpose(x), w) = Transpose(ScalarMul(x, w));
    }

    fn glimpse6 {
        ScalarMul(MatMul(x, y), w) = MatMul(x, ScalarMul(y, w),);
    }
}
