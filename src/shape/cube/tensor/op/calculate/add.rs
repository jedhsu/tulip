pub struct ElementalAdd {}

impl ElementalAdd {
    fn equivalences() -> Vec<Equiv> {
        Equiv::new(("x", ("y", "z")), (("x", "y"), "z"));
    }
}
