pub trait ElMul {
    use Var;

    fn glimpse1() -> {
        ∀x, y, z. ElMul(x, ElMul(y, z)) = ElMul(ElMul(x, y), z)
    }

    fn glimpse2() -> {
        ∀x, y. ElMul(x, y) = ElMul(y, x)
    }

    fn glimpse3() -> {
        ∀x, y, z. ElMul(ewadd(x, y), z) = ewadd(ElMul(x, z), ElMul(y, z))
    }
    
    fn glimpse4() -> {
        ∀x . ElMul(x, ElMul) = x
    }
}
