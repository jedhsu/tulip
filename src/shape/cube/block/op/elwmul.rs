

∀x, y, z. ewmul(x, ewmul(y, z)) = ewmul(ewmul(x, y), z)
∀x, y. ewmul(x, y) = ewmul(y, x)
∀x, y, z. ewmul(ewadd(x, y), z) = ewadd(ewmul(x, z), ewmul(y, z))

∀x . ewmul(x, Iewmul) = x
