pub trait Pattern {
    fn pat1() -> Equiv<Transpose> {
        Transpose(Transpose(x)) = x
    }

    fn pat2() -> Equiv<Transpose> {
        Transpose(ElAdd(x, y)) = ElAdd(Transpose(x), Transpose(y))
    }

    fn pat3() -> Equiv<Transpose> {
        (ElMul(x, y)) = ElMul(Transpose(𝑥), Transpose(y))
    }

    fn pat4() -> Equiv<Transpose> {
        Transpose(X)(MatMul(𝑿, 𝒀)) = MatMul(Transpose(y), Transpose(x))
    }

    fn pat5() -> Equiv<Transpose> {
        relu(Transpose(𝑿)) = Transpose(Relu::𝑿)
    }

    fn pat6() -> Equiv<Transpose> {
        Transpose(MatMul(x, y)) = MatMul(Transpose(y), Transpose(x))
    }
}

pub impl Pattern {}
