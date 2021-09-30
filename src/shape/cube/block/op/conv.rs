/// Equivalences for Conv
pub trait Glimpse {
    fn glimpse1() -> Equiv<Conv, Conv> {
        Equiv(
            Conv(s, p, c, ScalarMul(𝚇, 𝑤), 𝙮),
            Conv(s, p, c, 𝚇, ScalarMul(𝙮,𝑤)),
        )
    }

    fn glimpse2() -> Equiv<Conv, Conv> {
        ∀s, p, 𝚇, 𝙮, 𝚠. ScalarMul(Conv(s, p, Anone, 𝚇, 𝙮), w) = Conv(s, p, Anone, ScalarMul(𝚇, w), 𝙮);
    }

    fn glimpse3() -> Equiv<Conv, Conv> {
        Conv(s, p, Anone, 𝚇, ElAdd(𝙮, 𝒁)) = ElAdd(Conv(s, p, Anone, 𝚇, 𝙮), Conv(s, p, Anone, 𝚇, 𝒁),)
    }

    fn glimpse4() -> Equiv<Conv, Conv> {
        Conv(s, p, Anone, ElAdd(𝚇, 𝙮), 𝒁) = ElAdd(Conv(s, p, Anone, 𝚇, 𝒁), Conv(s, p, Anone, 𝙮, 𝒁))
    }

    fn glimpse5() {
        ∀s, c, k, 𝚇, 𝙮. Conv(s, Psame, c, 𝚇, 𝙮) = Conv(s, Psame, c, 𝚇, Enlarge(k, 𝙮)),
    }

    fn glimpse6() {
        ∀s, p, 𝚇, 𝙮. Conv(s, p, Arelu, 𝚇, 𝙮) = relu(Conv(s, p, Anone, 𝚇, 𝙮))
    }

} 

/// Sick
macro_rules! 𝙵𝚗 {
}

macro_rules! 𝚃𝚎𝚗 {
}

/// semantics for the dependently typed tensor.
macro_rules! TensorType {

}
/// Macro for params in ml and all the boilerplate!
   
𝚃𝚎𝚗!
(A ==>
[1 2 3
 4 5 6
 7 8 9]
);


/// Can create a dependent type check!

// ∀s, p, x, k. Conv(s, p, Anone, x, Cpool(k)) = poolavg(k, s, p, x)
//
// ∀k, x . Conv(1, Psame, Anone, x, IConv(k)) = x
