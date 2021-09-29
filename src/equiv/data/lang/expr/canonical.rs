pub trait Canonical {
    fn canonize(&self);
    fn decanonize(&self);
}
