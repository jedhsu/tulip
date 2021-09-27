use spaces::Discrete;

pub trait EqGraph: ProductSpace<{
    fn is_representing(&self, term: &Term) -> bool;
    fn populate(&self);
}


