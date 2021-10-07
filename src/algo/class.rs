use model::equiv::Isometrizer;

pub trait EqClass: X
where
    X: T,

    T: Isometrizer,
{
    pub type EqNodes;

    fn representations(
        &self,
        term: &Term,
    ) -> {
        let 
    }
}
