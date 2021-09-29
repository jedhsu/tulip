pub trait Glimpse {
    fn glimpse1() -> Equiv<Concat, Concat> {
∀x, y, z, w. concat(0, concat(1, x, y), concat(1, z, w)) = concat(1, concat(0, x, z), concat(0, y, w))
    }

    fn glimpse2() -> Equiv<Concat, Concat> {
    ∀a, x, y, w. concat(a, smul(x, w), smul(y, w)) = smul(concat(a, x, y), w)
    }


    fn glimpse3() -> Equiv<Concat, Concat> {
∀a, x, y, z, w. concat(a, ewadd(x, y), ewadd(z, w)) = ewadd(concat(a, x, z), concat(a, y, w))
    }

    fn glimpse5() -> Equiv<Concat, Concat> {
∀a, x, y, z, w. concat(a, ewmul(x, y), ewmul(z, w)) = ewmul(concat(a, x, z), concat(a, y, w))
    }

    fn glimpse6() -> Equiv<Concat, Concat> {
∀a, x, y. concat(a, relu(x), relu(y)) = relu(concat(a, x, y))
    }

    fn glimpse7() -> Equiv<Concat, Concat> {
∀x, y. concat(1, transpose(x), transpose(y)) = transpose(concat(0, x, y))
    }

    fn glimpse8() -> Equiv<Concat, Concat> {
∀x, y, z. concat(1, matmul(x, y), matmul(x, z)) = matmul(x, concat(1, y, z))
    }

}

    fn glimpse9() -> Equiv<Concat, Concat> {
∀s, p, c, x, y, z. concat(0, conv(s, p, c, x, z), conv(s, p, c, y, z)) = conv(s, p, c, concat(0, x, y), z)
    }

    fn glimpse10() -> Equiv<Concat, Concat> {
∀s, p, c, x, y, z. concat(1, conv(s, p, c, x, y), conv(s, p, c, x, z)) = conv(s, p, c, x, concat(0, y, z))
    }

    fn glimpse11() -> Equiv<Concat, Concat> {
∀s, p, x, y, z, w. conv(s, p, Anone,concat(1, x, z), concat(1, y, w)) =
ewadd(conv(s, p, Anone, x, y), conv(s, p, Anone, z, w))
    }

    fn glimpse12() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. concat(1, poolavg(k, s, p, x), poolavg(k, s, p, y)) = poolavg(k, s, p, concat(1, x, y))
    }

    fn glimpse13() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. concat(0, poolmax(k, s, p, x), poolmax(k, s, p, y)) = poolmax(k, s, p, concat(0, x, y))
    }

    fn glimpse14() -> Equiv<Concat, Concat> {
∀k, s, p, x, y. concat(1, poolmax(k, s, p, x), poolmax(k, s, p, y)) = poolmax(k, s, p, concat(1, x, y))
    }
