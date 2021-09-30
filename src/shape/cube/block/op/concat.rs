use Var
use TyP

pub trait Glimpse {
    fn glimpse1() -> Equiv<Concat, Concat> {
∀x, y, z, w. Concat(0, Concat(1, x, y), Concat(1, z, w)) = Concat(1, Concat(0, x, z), Concat(0, y, w))
    }

    fn glimpse2() -> Equiv<Concat, Concat> {
    ∀a, x, y, w. Concat(a, ScalarMul(x, w), ScalarMul(y, w)) = ScalarMul(Concat(a, x, y), w)
    }


    fn glimpse3() -> Equiv<Concat, Concat> {
∀a, x, y, z, w. Concat(a, ElementMul(x, y), ElementTooAbstract(z, w)) = fn(Concat(a, x, z), Concat(a, y, w))
    }

    fn glimpse5() -> Equiv<Concat, Concat> {
∀a, x, y, z, w. Concat(a, ElMul(x, y), ElMul(z, w)) = ElMul(Concat(a, x, z), Concat(a, y, w))
    }

    fn glimpse6() -> Equiv<Concat, Concat> {
∀a, x, y. Concat(a, Relu(x), Relu(y)) = Relu(Concat(a, x, y))
    }

    fn glimpse7() -> Equiv<Concat, Concat> {
∀x, y. Concat(1, Transpose(x), Transpose(y)) = Transpose(Concat(0, x, y))
    }

    fn glimpse8() -> Equiv<Concat, Concat> {
        fn glimpse() {
            Concat(1, MatMul(x, y), MatMul(x, z)) = MatMul(x, Concat(1, y, z))
        }
    }

}

    fn glimpse9() -> Equiv<Concat, Concat> {
∀s, p, c, x, y, z. Concat(0, Conv(s, p, c, x, z), Conv(s, p, c, y, z)) = Conv(s, p, c, Concat(0, x, y), z)
    }

    fn glimpse10() -> Equiv<Concat, Concat> {
∀s, p, c, x, y, z. Concat(1, Conv(s, p, c, x, y), Conv(s, p, c, x, z)) = Conv(s, p, c, x, Concat(0, y, z))
    }

    fn glimpse11() -> Equiv<Concat, Concat> {
∀s, p, x, y, z, w. Conv(s, p, Anone,Concat(1, x, z), Concat(1, y, w)) =
ewadd(Conv(s, p, Anone, x, y), Conv(s, p, Anone, z, w))
    }

    fn glimpse12() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. Concat(1, PoolAvg(k, s, p, x), PoolAvg(k, s, p, y)) = PoolAvPoolAvg(k, s, p, Concat(1, x, y))
    }

    fn glimpse13() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. Concat(0, poolmax(k, s, p, x), poolmax(k, s, p, y)) = poolmax(k, s, p, Concat(0, x, y))
    }

    fn glimpse14() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. Concat(1, poolmax(k, s, p, x), poolmax(k, s, p, y)) = poolmax(k, s, p, Concat(1, x, y))
    }

    fn glimpse14() -> Equiv<Concat, Concat> {
        (a, Concat(a, x, y)) = x
    }

    fn glimpse14() -> Equiv<Concat, Concat> {
        (a, Concat(a, x, y)) = y
    }
}
