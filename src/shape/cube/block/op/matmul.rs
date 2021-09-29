pub trait Glimpse {
    fn glimpse1() -> {
        ∀x, y, z. matmul(x, matmul(y, z)) = matmul(matmul(x, y), z)
    }

    fn glimpse2() -> {
∀x, y, z. matmul(x, ewadd(y, z)) = ewadd(matmul(x, y), matmul(x, z))
    }

    fn glimpse3() -> {
∀x . matmul(x, Imatmul) = x
    }
    
    fn glimpse4() -> {
∀x, y, z, w. matmul(concat(1, x, z), concat(0, y, w)) = ewadd(matmul(x, y), matmul(z, w))
    }
}

