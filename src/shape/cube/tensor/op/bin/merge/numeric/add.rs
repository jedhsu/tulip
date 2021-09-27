pub struct Add {}

impl Add {
    fn equivalences() -> Vec<Equiv> {
        Equiv::new(("x", ("y", "z")), (("x", "y"), "z"));
    }
}
