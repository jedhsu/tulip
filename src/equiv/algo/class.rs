use model::equiv::Isometrizer;

pub trait EqClass: X
where
    X: T,

    T: Isometrizer,
{
    fn is_representing(
        &self,
        term: &Term,
    ) -> bool;
}
