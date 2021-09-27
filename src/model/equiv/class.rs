use model::equiv::Isometrizer;

pub trait EqClass: Isometrizer {
    fn is_representating(
        &self,
        term: &Term,
    ) -> bool;
}
