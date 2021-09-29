/// Equivalences for Conv
pub trait Glimpse {
    fn glimpse1() -> Equiv<Conv, Conv> {
        Equiv(
            Conv(s, p, c, ScalarMul(x, w), y),
            Conv(s, p, c, x, ScalarMul(y, w)),
        )
    }

    fn glimpse1() -> Equiv<Conv, Conv> {
        ∀s, p, x, y, w. smul(conv(s, p, Anone, x, y), w) = conv(s, p, Anone, smul(x, w), y);
    }

    fn glimpse1() -> Equiv<Conv, Conv> {
∀s, p, x, y, z. conv(s, p, Anone, x, ewadd(y, z)) = ewadd(conv(s, p, Anone, x, y), conv(s, p, Anone, x, z))
    }

    fn glimpse1() -> Equiv<Conv, Conv> {
∀s, p, x, y, z. conv(s, p, Anone, ewadd(x, y), z) = ewadd(conv(s, p, Anone, x, z), conv(s, p, Anone, y, z))
    }

// ∀s, c, k, x, y. conv(s, Psame, c, x, y) = conv(s, Psame, c, x, enlarge(k, y)),

// ∀s, p, x, y. conv(s, p, Arelu, x, y) = relu(conv(s, p, Anone, x, y))

// ∀x . relu(transpose(x)) = transpose(relu(x))

// ∀s, p, x, k. conv(s, p, Anone, x, Cpool(k)) = poolavg(k, s, p, x)
//
// ∀k, x . conv(1, Psame, Anone, x, Iconv(k)) = x
