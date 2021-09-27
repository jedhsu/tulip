use egg::{define_language, Id};

define_language! {
    pub enum Tensor {
        " ⤉ " = Differential([Id]),
        " ⤈ " = Integral([Id]),

        " + " = EwAdd([Id; 2])
        " ⚪" = EwMul([Id; 2])

        " ⨉ " = Mul([Id; 2])  /// I think wrog type hre

        " ⏣	" = Conv([Id; 6])

        " x " = Relu
        " x " = Tanh
        " ʃ " = Sigmoid

        " ⨁ " = MaxPool
        " x " = AvgPool

        " x " = Transpose

        " x " = ZeroPad

        "  ̈ "  = Concat

        " x " = Split

        " x " = Left

        " x " = Right

        " x " = Merge

        " x " = Reshape

        " x " = Weight
        " ▮ " = InputTensor(Id),

        Constant(Constant),
        Symbol(Symbol),
    }
}
