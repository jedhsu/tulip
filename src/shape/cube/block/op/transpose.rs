pub trait Glimpse {
    fn glimpse1() -> Equiv<Transpose> {
∀x . transpose(transpose(x)) = x
    }
    
    fn glimpse2() -> Equiv<Transpose> {
∀x, y. transpose(ewadd(x, y)) = ewadd(transpose(x), transpose(y))
    }


    fn glimpse3() -> Equiv<Transpose> {
∀x, y. transpose(ewmul(x, y)) = ewmul(transpose(x), transpose(y))
    }
